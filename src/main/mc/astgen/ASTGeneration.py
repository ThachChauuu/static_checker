# /*
# / @problem:
# /   ASTGenneration
# / @author:
# /   FullName: Châu Ngọc Thạch <51303740@hcmut.edu.vn>
# /   ID: 51303740
# */

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *


class ASTGeneration(MCVisitor):
    
    def visitProgram(self, ctx: MCParser.ProgramContext):
        results = []
        for i in range(len(ctx.decls())):
            if ctx.decls(i).vardecl():
                for item in self.visit(ctx.decls(i)):
                    results.append(item)
            else:
                results.append(self.visit(ctx.decls(i)))
        return Program(results)
    
    def visitDecls(self, ctx: MCParser.DeclsContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return self.visit(ctx.funcdecl())

    def visitPrimitiveType(self, ctx: MCParser.PrimitiveTypeContext):
        if ctx.BOOLTYPE():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        else:
            return StringType()

    def visitVardecl(self, ctx: MCParser.VardeclContext):
        results = []
        for variable in self.visit(ctx.variables()):
            if variable[1]:
                results.append(VarDecl(variable[0], ArrayType(variable[1], self.visit(ctx.primitiveType()))))
            else:
                results.append(
                    VarDecl(variable[0], self.visit(ctx.primitiveType())))
        return results

    def visitVariables(self, ctx: MCParser.VariablesContext):
        return ([self.visit(x) for x in ctx.variable()] if ctx.variable() else [])

    def visitVariable(self, ctx: MCParser.VariableContext):
        if ctx.INTLIT():
            return Id(ctx.ID().getText()), IntLiteral(int(ctx.INTLIT().getText()))
        else:
            return Id(ctx.ID().getText()), None

    def visitFuncdecl(self, ctx: MCParser.FuncdeclContext):
        funcName = self.visit(ctx.funcname())
        paramList = self.visit(ctx.paramlist()) if ctx.paramlist() else []
        funcType = self.visit(ctx.functype())
        funcBlock = self.visit(ctx.blockstmt())
        return FuncDecl(funcName, paramList, funcType, funcBlock)

    def visitFunctype(self, ctx: MCParser.FunctypeContext):
        if ctx.VOIDTYPE():
            return VoidType()
        elif ctx.primitiveType():
            return self.visit(ctx.primitiveType())
        else:
            return self.visit(ctx.arrPointType())

    def visitArrPointType(self, ctx: MCParser.ArrPointTypeContext):
        return ArrayPointerType(self.visit(ctx.primitiveType()))

    def visitFuncname(self, ctx: MCParser.FuncnameContext):
        return Id(ctx.ID().getText())

    def visitParamlist(self, ctx: MCParser.ParamlistContext):
        results = []
        for param in ctx.paramdecl():
            results.append(self.visit(param))
        return results

    def visitParamdecl(self, ctx: MCParser.ParamdeclContext):
        if ctx.LS():
            return VarDecl(Id(ctx.ID().getText()), ArrayPointerType(self.visit(ctx.primitiveType())))
        else:
            return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.primitiveType()))

    def visitBlockstmt(self, ctx: MCParser.BlockstmtContext):
        decl = self.visit(ctx.vardeclList()) if ctx.vardeclList() else []
        stmt = self.visit(ctx.stmtList()) if ctx.stmtList() else []
        return Block(decl, stmt)

    def visitVardeclList(self, ctx: MCParser.VardeclListContext):
        results = []
        for i in range(len(ctx.vardecl())):
            action = self.visit(ctx.vardecl(i))
            for item in action:
                results.append(item)
        return results

    def visitStmtList(self, ctx: MCParser.StmtListContext):
        results = []
        for i in range(len(ctx.stmt())):
            action = self.visit(ctx.stmt(i))
            results.append(action)
        return results

    def visitStmt(self, ctx: MCParser.StmtContext):
        if ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.dowhilestmt():
            return self.visit(ctx.dowhilestmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.exprstmt():
            return self.visit(ctx.exprstmt())
        else:
            return self.visit(ctx.blockstmt())
            
    def visitIfstmt(self, ctx: MCParser.IfstmtContext):
        expr = self.visit(ctx.expr())
        stmtInIf = self.visit(ctx.stmt(0))
        if ctx.stmt(1):
            return If(expr, stmtInIf, self.visit(ctx.stmt(1)))
        else:
            return If(expr, stmtInIf)

    def visitForstmt(self, ctx: MCParser.ForstmtContext):
        expr0 = self.visit(ctx.expr(0))
        expr1 = self.visit(ctx.expr(1))
        expr2 = self.visit(ctx.expr(2))
        loop = self.visit(ctx.stmt())
        return For(expr0, expr1, expr2, loop)

    def visitDowhilestmt(self, ctx: MCParser.DowhilestmtContext):
        stmtList = []
        expr = self.visit(ctx.expr())
        for i in range(len(ctx.stmt())):
            action = self.visit(ctx.stmt(i))
            stmtList.append(action)
        return Dowhile(stmtList, expr)

    def visitBreakstmt(self, ctx: MCParser.BreakstmtContext):
        return Break()

    def visitContinuestmt(self, ctx: MCParser.ContinuestmtContext):
        return Continue()

    def visitReturnstmt(self, ctx: MCParser.ReturnstmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return()

    def visitExprstmt(self, ctx: MCParser.ExprstmtContext):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx: MCParser.ExprContext):
        if ctx.ASSIGN():
            left = self.visit(ctx.expr_1())
            right = self.visit(ctx.expr())
            return BinaryOp("=", left, right)
        else:
            return self.visit(ctx.expr_1())

    def visitExpr_1(self, ctx: MCParser.Expr_1Context):
        if ctx.OR():
            left = self.visit(ctx.expr_1())
            right = self.visit(ctx.expr_2())
            return BinaryOp("||", left, right)
        else:
            return self.visit(ctx.expr_2())

    def visitExpr_2(self, ctx: MCParser.Expr_2Context):
        if ctx.AND():
            left = self.visit(ctx.expr_2())
            right = self.visit(ctx.expr_3())
            return BinaryOp("&&", left, right)
        else:
            return self.visit(ctx.expr_3())

    def visitExpr_3(self, ctx: MCParser.Expr_3Context):
        if ctx.EQ():
            return BinaryOp("==", self.visit(ctx.expr_4(0)), self.visit(ctx.expr_4(1)))
        elif ctx.NEQ():
            return BinaryOp("!=", self.visit(ctx.expr_4(0)), self.visit(ctx.expr_4(1)))
        else:
            return self.visit(ctx.expr_4(0))

    def visitExpr_4(self, ctx: MCParser.Expr_4Context):
        if ctx.LT():
            return BinaryOp("<", self.visit(ctx.expr_5(0)), self.visit(ctx.expr_5(1)))
        elif ctx.GT():
            return BinaryOp(">", self.visit(ctx.expr_5(0)), self.visit(ctx.expr_5(1)))
        elif ctx.LTEQ():
            return BinaryOp("<=", self.visit(ctx.expr_5(0)), self.visit(ctx.expr_5(1)))
        elif ctx.GTEQ():
            return BinaryOp(">=", self.visit(ctx.expr_5(0)), self.visit(ctx.expr_5(1)))
        else:
            return self.visit(ctx.expr_5(0))

    def visitExpr_5(self, ctx: MCParser.Expr_5Context):
        if ctx.ADD():
            return BinaryOp("+", self.visit(ctx.expr_5()), self.visit(ctx.expr_6()))
        elif ctx.SUB():
            return BinaryOp("-", self.visit(ctx.expr_5()), self.visit(ctx.expr_6()))
        else:
            return self.visit(ctx.expr_6())

    def visitExpr_6(self, ctx: MCParser.Expr_6Context):
        if ctx.DIV():
            return BinaryOp("/", self.visit(ctx.expr_6()), self.visit(ctx.expr_7()))
        elif ctx.MUL():
            return BinaryOp("*", self.visit(ctx.expr_6()), self.visit(ctx.expr_7()))
        elif ctx.MOD():
            return BinaryOp("%", self.visit(ctx.expr_6()), self.visit(ctx.expr_7()))
        else:
            return self.visit(ctx.expr_7())

    def visitExpr_7(self, ctx: MCParser.Expr_7Context):
        if ctx.SUB():
            return UnaryOp("-", self.visit(ctx.expr_7()))
        elif ctx.NOT():
            return UnaryOp("!", self.visit(ctx.expr_7()))
        else:
            return self.visit(ctx.expr_8())

    def visitExpr_8(self, ctx: MCParser.Expr_8Context):
        if ctx.expr():
            return ArrayCell(self.visit(ctx.expr_9()), self.visit(ctx.expr()))
        else:
            return self.visit(ctx.expr_9())

    def visitExpr_9(self, ctx: MCParser.Expr_9Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT():
            if ctx.BOOLLIT().getText() == "true":
                return BooleanLiteral(True)
            return BooleanLiteral(False)
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        else:
            return Id(ctx.ID().getText())


    def visitFunccall(self, ctx: MCParser.FunccallContext):
        funcId = Id(ctx.ID().getText())
        funcPa = []
        if ctx.expr():
            for i in range(len(ctx.expr())):
                action = self.visit(ctx.expr(i))
                funcPa.append(action)
            return CallExpr(funcId, funcPa)
        else:
            return CallExpr(funcId, [])
