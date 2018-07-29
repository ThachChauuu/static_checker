
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    getInt = Symbol("getInt", MType([], IntType()))
    putInt = Symbol("putInt", MType([IntType()], VoidType()))
    putIntLn = Symbol("putIntLn", MType([IntType()], VoidType()))
    getFloat = Symbol("getFloat", MType([], FloatType()))
    putFloat = Symbol("putFloat", MType([FloatType()], VoidType()))
    putFloatLn = Symbol("putFloatLn", MType([FloatType], VoidType()))
    putBool = Symbol("putBool", MType([BoolType], VoidType()))
    putBoolLn = Symbol("putBoolLn", MType([BoolType], VoidType()))
    putString = Symbol("putString", MType([StringType()], VoidType()))
    putStringLn = Symbol("putStringLn", MType([StringType()], VoidType()))
    putLn = Symbol("putLn", MType([], VoidType()))

    global_envi = [getInt, putInt, putIntLn, getFloat, putFloat,
                   putFloatLn, putBool, putBoolLn, putString, putStringLn, putLn]
    scope_index = [0]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def createSymbol(self, decl):
        if type(decl) is VarDecl:
            return Symbol(decl.variable.name, MType([], decl.varType))
        else:
            paramTypes = []
            for i in decl.param:
                paramTypes.append(i.varType)
            funcType = decl.returnType
            return Symbol(decl.name.name, MType([paramTypes], funcType))

    def enterScope(self, i, ins_scope_idx: list):
        ins_scope_idx.append(i)

    def insertSymbol(self, symbol: Symbol, ins_glolist: list):
        ins_glolist.append(symbol)

    def exitScope(self, start, end):
        del self.global_envi[start:end]
        del self.scope_index[-1]

    def lookupId(self, id, glo_envs: list):
        for i in reversed(glo_envs):
            if i.name == id:
                # return i.mtype.rettype
                return i
            return None
                    
    def checkExpr(self, expr, glo_envs):
        if type(expr) is Id:
            if self.lookupId(expr.name, glo_envs):
                return self.lookupId(expr.name, glo_envs).mtype.rettype
            else:
                raise Undeclared(Identifier(), expr.name)

        elif type(expr) is IntLiteral:
            return IntType()

        elif type(expr) is BooleanLiteral:
            return BoolType()

        elif type(expr) is FloatLiteral:
            return FloatType()

        elif type(expr) is StringLiteral:
            return StringType()

        elif type(expr) is ArrayCell:
            arrtype = self.checkExpr(expr.arr, glo_envs)
            idxtype = self.checkExpr(expr.idx, glo_envs)
            if arrtype == ArrayType() and idxtype == IntType():
                return ArrayType()
            else:
                raise TypeMismatchInExpression(expr)

        elif type(expr) is UnaryOp:
            rettype = checkExpr(expr.body, glo_envs)
            if rettype == BoolType() and expr.op == "!":
                return BoolType()
            elif rettype == IntType() and expr.op == "-":
                return IntType()
            elif rettype == FloatType() and expr.op == "-":
                return FloatType()
            else:
                raise TypeMismatchInExpression(expr)

        elif type(expr) is BinaryOp:
            ltype = self.checkExpr(expr.left, glo_envs)
            rtype = self.checkExpr(expr.right, glo_envs)
            if expr.op == "<" or expr.op == ">" or expr.op == "<=" or expr.op == ">=":
                if (ltype == IntType() and rtype == IntType()) or (ltype == IntType() and rtype == FloatType()) or (ltype == FloatType() and rtype == IntType()) or (ltype == FloatType() and rtype == FloatType()):
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(expr)
            elif expr.op == "==" or expr.op == "!=":
                if ltype == rtype:
                    if ltype == VoidType():
                        raise TypeMismatchInExpression(expr)
                    else:
                        return BoolType()
                else:
                    raise TypeMismatchInExpression(expr)
            elif expr.op == "+" or expr.op == "-" or expr.op == "*" or expr.op == "/":
                if ltype == IntType() and rtype == IntType():
                    return IntType()
                elif (ltype == IntType() and rtype == FloatType()) or (ltype == FloatType() and rtype == IntType()) or (ltype == FloatType() and rtype == FloatType()):
                    return FloatType()
                else:
                    raise TypeMismatchInExpression(expr)
            elif expr.op == "%":
                if ltype == IntType() and rtype == IntType():
                    return IntType()
                else:
                    raise TypeMismatchInExpression(expr)
            else:
                raise TypeMismatchInExpression(expr)

        elif type(expr) is CallExpr:               # CallExpr
            sym = self.lookupId(expr.method.name, glo_envs)
            if sym:
                if expr.param.size() == sym.mtype.partype.size():
                    for i in range(expr.param.size()):
                        ptype = self.checkExpr(expr.param[i], glo_envs)
                        if ptype != sym.mtype.partype[i]:
                            raise TypeMismatchInStatement(expr)
                else:
                    raise TypeMismatchInStatement(expr)
            else:
                raise Undeclared(Function(), expr.method.name)
            # if self.lookupId(expr.method.name, glo_envs):
            #     # return self.lookupId(expr.method.name, glo_envs)
            #     for i in expr.param:
            #         if self.lookupId(i.name, glo_envs) is None:
            #             raise Undeclared(Identifier(), i.name)
            # else:
            #     raise Undeclared(Function(), expr.method.name)
        else:
            return IntType()
            


    def visitProgram(self, ast, c):
        ins_glo_evns = c.copy()
        ins_scope_idxs = self.scope_index.copy()
        subs = []
        ins_scope_idxs.append(len(ins_glo_evns))
        for d in ast.decl:
            if type(d) is VarDecl:
                if self.lookup(d.variable.name, reversed(ins_glo_evns), lambda x: x.name):
                    raise Redeclared(Variable(), d.variable.name)
                ins_glo_evns.append(Symbol(d.variable.name, MType([], d.varType)))
            else:
                if self.lookup(d.name.name, reversed(ins_glo_evns), lambda x: x.name):
                    raise Redeclared(Function(), d.name.name)
                else:
                    ins_glo_evns.append(Symbol(d.name.name, MType([i.varType for i in d.param], d.returnType)))
                    ins_scope_idxs.append(len(ins_glo_evns))
                    subs = ins_glo_evns[len(ins_glo_evns): len(ins_glo_evns) + 1]
                    for p in d.param:
                        if self.lookup(p.variable.name, reversed(subs), lambda x: x.name):
                            raise Redeclared(Parameter(), p.variable.name)
                        subs.append(Symbol(p.variable.name, MType([], p.varType)))
                ins_glo_evns += subs
                c = ins_glo_evns.copy()
                self.scope_index = ins_scope_idxs.copy()
                self.visitBlock(d.body, ins_glo_evns)


    def visitBlock(self, ast, c):
        # ins_glo_evns = c.copy()
        # ins_scope_idxs = self.scope_index.copy()
        if ast.decl:
            for v in ast.decl:
                if self.lookup(v.variable.name, reversed(c), lambda x: x.name):
                    raise Redeclared(Variable(), v.variable.name)
                c.append(Symbol(v.variable.name, MType([], v.varType)))
        # c = ins_glo_evns.copy()
        if ast.stmt:      # check stmt
            # ins_glo_evns = c.copy()
            for st in ast.stmt:
                if type(st) is If:
                    etype = self.checkExpr(st.expr, c)
                    if etype != BoolType():
                        raise TypeMismatchInStatement(st)
                elif type(st) is For:
                    e1type = self.checkExpr(st.expr1, c)
                    e2type = self.checkExpr(st.expr2, c)
                    e3type = self.checkExpr(st.expr3, c)
                    if e1type != IntType() or e3type != IntType() or e2type != BoolType():
                        raise TypeMismatchInStatement(st)
                elif type(st) is Break:
                    pass
                elif type(st) is Continue:
                    pass
                elif type(st) is Return:
                   pass
                elif type(st) is Dowhile:
                    etype = self.checkExpr(st.exp, c)
                    if etype != BoolType():
                        raise TypeMismatchInStatement(st)
                elif type(st) is BinaryOp:
                    self.checkExpr(st, c)
                elif type(st) is UnaryOp:
                    self.checkExpr(st, c)
                elif type(st) is CallExpr:
                    self.checkExpr(st, c)
                elif type(st) is Id:
                    self.checkExpr(st, c)
                elif type(st) is ArrayCell:
                    self.checkExpr(st, c)
                else:
                    self.visitBlock(st, c)


    # def visitProgram(self, ast, c):
    #     ins_glolist = c.copy()
    #     ins_scope_idx = self.scope_index.copy()
    #     self.enterScope(len(ins_glolist), ins_scope_idx)
    #     for d in ast.decl:
    #         s = self.createSymbol(d)
    #         if self.lookup(s.name, reversed(ins_glolist), lambda x: x.name):
    #             if type(d) is VarDecl:
    #                 raise Redeclared(Variable(), s.name)
    #             raise Redeclared(Function(), s.name)
    #         else:
    #             self.insertSymbol(s, ins_glolist)
    #     c = ins_glolist.copy()
    #     self.scope_index = ins_scope_idx.copy()

    # def visitFuncDecl(self, ast, c):
    #     ins_glolist = c.copy()
    #     ins_scope_idx = self.scope_index.copy()
    #     self.enterScope(len(ins_glolist), ins_scope_idx)
    #     subs = ins_glolist[len(ins_glolist):len(ins_glolist)+1]
    #     for p in ast.body:
    #         s = self.createSymbol(p)
    #         if self.lookup(s.name, reversed(ins_glolist), lambda x: x.name):
    #             raise Redeclared(Parameter(), s.name)
    #         else:
    #             self.insertSymbol(s, subs)
    #     ins_glolist += subs
    #     for v in ast.body:
    #         raise MyTest(v.variable.name)
