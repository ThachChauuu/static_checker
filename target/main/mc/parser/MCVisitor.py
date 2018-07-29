# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decls.
    def visitDecls(self, ctx:MCParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitiveType.
    def visitPrimitiveType(self, ctx:MCParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variables.
    def visitVariables(self, ctx:MCParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#functype.
    def visitFunctype(self, ctx:MCParser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdecl.
    def visitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arrPointType.
    def visitArrPointType(self, ctx:MCParser.ArrPointTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcname.
    def visitFuncname(self, ctx:MCParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramlist.
    def visitParamlist(self, ctx:MCParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paramdecl.
    def visitParamdecl(self, ctx:MCParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockstmt.
    def visitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardeclList.
    def visitVardeclList(self, ctx:MCParser.VardeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmtList.
    def visitStmtList(self, ctx:MCParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifstmt.
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forstmt.
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continuestmt.
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakstmt.
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnstmt.
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exprstmt.
    def visitExprstmt(self, ctx:MCParser.ExprstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_1.
    def visitExpr_1(self, ctx:MCParser.Expr_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_2.
    def visitExpr_2(self, ctx:MCParser.Expr_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_3.
    def visitExpr_3(self, ctx:MCParser.Expr_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_4.
    def visitExpr_4(self, ctx:MCParser.Expr_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_5.
    def visitExpr_5(self, ctx:MCParser.Expr_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_6.
    def visitExpr_6(self, ctx:MCParser.Expr_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_7.
    def visitExpr_7(self, ctx:MCParser.Expr_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_8.
    def visitExpr_8(self, ctx:MCParser.Expr_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr_9.
    def visitExpr_9(self, ctx:MCParser.Expr_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funccall.
    def visitFunccall(self, ctx:MCParser.FunccallContext):
        return self.visitChildren(ctx)



del MCParser