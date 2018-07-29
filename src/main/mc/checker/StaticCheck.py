
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    # global_envi = [Symbol("getInt",MType([],IntType())),Symbol("putIntLn",MType([IntType()],VoidType()))]

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

    global_envi = [getInt, putInt, putIntLn, getFloat, putFloat, putFloatLn, putBool, putBoolLn, putString, putStringLn, putLn]
            
    def __init__(self,ast):
        self.ast = ast

    def lookupId(self, id, lst):
        pass

    # def checkExpr(self, expr, glst):
    #     if type(expr) is Id:
    #         pass
            
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        ins_glo_envi = self.global_envi.copy()
        for d in ast.decl:
            if type(d) is VarDecl:
                self.visitVarDecl(d, ins_glo_envi)
            else:
                self.visitFuncDecl(d, ins_glo_envi)

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable.name, c, lambda x: x.name):
            raise Redeclared(Variable(), ast.variable.name)
        else:
            c.append(Symbol(ast.variable.name, ast.varType))

    def visitFuncDecl(self, ast, c):
        if self.lookup(ast.name.name, c, lambda x: x.name):
            raise Redeclared(Function(), ast.name.name)
        else:
            c.append(Symbol(ast.name.name, MType([p.varType for p in ast.param] if ast.param else [], ast.returnType)))
        
        c.insert(len(c), [])
        for p in ast.param:
            if self.lookup(p.variable.name, c[len(c)-1], lambda x: x.name):
                raise Redeclared(Parameter(), p.variable.name)
            else:
                c[len(c)-1].append(Symbol(p.variable.name, p.varType))
        self.visitBlock(ast.body, c[len(c)-1])
        # exit scope
        del c[-1]

    
    def visitBlock(self, ast, c):
        for x in ast.decl:
            self.visitVarDecl(x,c)
        for st in ast.stmt:
            if type(st) is If:
                self.visitIf(st, c)

    def visitIf(self, ast, c):
        pass



    # # open a scope, with initial [ioms]
    # def enter_scope(self):
    #     return []

    # # insert a symbol into symbol list
    # def insert_symbol(self, s, sl):
    #     sl.append(s)

    # # lookup a id into reference
    # def lookup_id_into_genvs(self, id, rel):
    #     for ls in reversed(rel):
    #         for s in ls:
    #             if id == s.name:
    #                 return s
    #             else:
    #                 return None

    # #  lookup a id into scope its
    # def lookup_id_into_syms(self, id, sl):
    #     for s in sl:
    #         if id == s.name:
    #             return s
    #         else:
    #             return None

    # def visitProgram(self, ast, c):
    #     ins_genvs = c.copy()
    #     # ls is list symbol, using to check a decl
    #     ins_sl = self.enter_scope()
    #     ins_sl.append([x for x in self.ioms])
    #     for d in ast.decl:
    #         if type(d) is VarDecl:
    #             if self.lookup_id_into_syms(d.variable.name, ins_sl):
    #                 print(len(ins_sl))
    #                 raise Redeclared(Variable(), d.variable.name)
    #             ins_sl.append(Symbol(d.variable.name, MType([], d.varType)))
    #     # ins_genvs is list reference enviroment, using to check call stmt, id, ...
    #     ins_genvs.append(ins_sl)
    #     c = ins_genvs.copy()
                    
        

    # def visitProgram(self,ast, c):    
    #     return [self.visit(x,c) for x in ast.decl]

    # def visitFuncDecl(self,ast, c): 
    #     return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt)) 
    

    # def visitCallExpr(self, ast, c): 
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
        
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype

    # def visitIntLiteral(self,ast, c): 
    #     return IntType()
    

