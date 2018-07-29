# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u01b0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3&\3\'\6\'\u00e2\n\'\r\'\16\'\u00e3")
        buf.write("\3(\6(\u00e7\n(\r(\16(\u00e8\3(\3(\7(\u00ed\n(\f(\16(")
        buf.write("\u00f0\13(\3(\3(\5(\u00f4\n(\3(\6(\u00f7\n(\r(\16(\u00f8")
        buf.write("\5(\u00fb\n(\3(\7(\u00fe\n(\f(\16(\u0101\13(\3(\3(\6(")
        buf.write("\u0105\n(\r(\16(\u0106\3(\3(\5(\u010b\n(\3(\6(\u010e\n")
        buf.write("(\r(\16(\u010f\5(\u0112\n(\3(\6(\u0115\n(\r(\16(\u0116")
        buf.write("\3(\3(\5(\u011b\n(\3(\6(\u011e\n(\r(\16(\u011f\5(\u0122")
        buf.write("\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\7)\u0136\n)\f)\16)\u0139\13)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\5*\u0147\n*\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\7,\u0161")
        buf.write("\n,\f,\16,\u0164\13,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-")
        buf.write("\3-\3-\3-\3-\3-\3-\3-\3-\3-\7-\u017a\n-\f-\16-\u017d\13")
        buf.write("-\3-\3-\3.\3.\3.\3.\7.\u0185\n.\f.\16.\u0188\13.\3.\3")
        buf.write(".\3.\3.\3.\3.\7.\u0190\n.\f.\16.\u0193\13.\3.\7.\u0196")
        buf.write("\n.\f.\16.\u0199\13.\5.\u019b\n.\3.\3.\3/\6/\u01a0\n/")
        buf.write("\r/\16/\u01a1\3/\3/\3\60\6\60\u01a7\n\60\r\60\16\60\u01a8")
        buf.write("\3\60\7\60\u01ac\n\60\f\60\16\60\u01af\13\60\4\u0186\u0197")
        buf.write("\2\61\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61\3\2\f\3\2\62;\4\2GGgg\4\2--/")
        buf.write("/\6\2\f\f\17\17$$^^\b\2%&()ABbb~~\u0080\u0080\4\2$$pp")
        buf.write("\4\2\f\f\17\17\4\2\n\f\"\"\5\2C\\aac|\6\2\62;C\\aac|\2")
        buf.write("\u01e3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\3a\3\2\2\2\5e\3\2\2\2\7m\3\2\2\2")
        buf.write("\tr\3\2\2\2\13y\3\2\2\2\r\177\3\2\2\2\17\u0088\3\2\2\2")
        buf.write("\21\u008d\3\2\2\2\23\u0091\3\2\2\2\25\u0094\3\2\2\2\27")
        buf.write("\u009b\3\2\2\2\31\u009e\3\2\2\2\33\u00a4\3\2\2\2\35\u00a6")
        buf.write("\3\2\2\2\37\u00a8\3\2\2\2!\u00aa\3\2\2\2#\u00ac\3\2\2")
        buf.write("\2%\u00ae\3\2\2\2\'\u00b0\3\2\2\2)\u00b3\3\2\2\2+\u00b6")
        buf.write("\3\2\2\2-\u00b9\3\2\2\2/\u00bc\3\2\2\2\61\u00be\3\2\2")
        buf.write("\2\63\u00c0\3\2\2\2\65\u00c3\3\2\2\2\67\u00c6\3\2\2\2")
        buf.write("9\u00c8\3\2\2\2;\u00ca\3\2\2\2=\u00cc\3\2\2\2?\u00ce\3")
        buf.write("\2\2\2A\u00d0\3\2\2\2C\u00d2\3\2\2\2E\u00d4\3\2\2\2G\u00d6")
        buf.write("\3\2\2\2I\u00d8\3\2\2\2K\u00da\3\2\2\2M\u00e1\3\2\2\2")
        buf.write("O\u0121\3\2\2\2Q\u0123\3\2\2\2S\u0146\3\2\2\2U\u0148\3")
        buf.write("\2\2\2W\u014b\3\2\2\2Y\u0167\3\2\2\2[\u019a\3\2\2\2]\u019f")
        buf.write("\3\2\2\2_\u01a6\3\2\2\2ab\7k\2\2bc\7p\2\2cd\7v\2\2d\4")
        buf.write("\3\2\2\2ef\7d\2\2fg\7q\2\2gh\7q\2\2hi\7n\2\2ij\7g\2\2")
        buf.write("jk\7c\2\2kl\7p\2\2l\6\3\2\2\2mn\7x\2\2no\7q\2\2op\7k\2")
        buf.write("\2pq\7f\2\2q\b\3\2\2\2rs\7u\2\2st\7v\2\2tu\7t\2\2uv\7")
        buf.write("k\2\2vw\7p\2\2wx\7i\2\2x\n\3\2\2\2yz\7h\2\2z{\7n\2\2{")
        buf.write("|\7q\2\2|}\7c\2\2}~\7v\2\2~\f\3\2\2\2\177\u0080\7e\2\2")
        buf.write("\u0080\u0081\7q\2\2\u0081\u0082\7p\2\2\u0082\u0083\7v")
        buf.write("\2\2\u0083\u0084\7k\2\2\u0084\u0085\7p\2\2\u0085\u0086")
        buf.write("\7w\2\2\u0086\u0087\7g\2\2\u0087\16\3\2\2\2\u0088\u0089")
        buf.write("\7g\2\2\u0089\u008a\7n\2\2\u008a\u008b\7u\2\2\u008b\u008c")
        buf.write("\7g\2\2\u008c\20\3\2\2\2\u008d\u008e\7h\2\2\u008e\u008f")
        buf.write("\7q\2\2\u008f\u0090\7t\2\2\u0090\22\3\2\2\2\u0091\u0092")
        buf.write("\7k\2\2\u0092\u0093\7h\2\2\u0093\24\3\2\2\2\u0094\u0095")
        buf.write("\7t\2\2\u0095\u0096\7g\2\2\u0096\u0097\7v\2\2\u0097\u0098")
        buf.write("\7w\2\2\u0098\u0099\7t\2\2\u0099\u009a\7p\2\2\u009a\26")
        buf.write("\3\2\2\2\u009b\u009c\7f\2\2\u009c\u009d\7q\2\2\u009d\30")
        buf.write("\3\2\2\2\u009e\u009f\7y\2\2\u009f\u00a0\7j\2\2\u00a0\u00a1")
        buf.write("\7k\2\2\u00a1\u00a2\7n\2\2\u00a2\u00a3\7g\2\2\u00a3\32")
        buf.write("\3\2\2\2\u00a4\u00a5\7-\2\2\u00a5\34\3\2\2\2\u00a6\u00a7")
        buf.write("\7/\2\2\u00a7\36\3\2\2\2\u00a8\u00a9\7,\2\2\u00a9 \3\2")
        buf.write("\2\2\u00aa\u00ab\7\61\2\2\u00ab\"\3\2\2\2\u00ac\u00ad")
        buf.write("\7#\2\2\u00ad$\3\2\2\2\u00ae\u00af\7\'\2\2\u00af&\3\2")
        buf.write("\2\2\u00b0\u00b1\7~\2\2\u00b1\u00b2\7~\2\2\u00b2(\3\2")
        buf.write("\2\2\u00b3\u00b4\7(\2\2\u00b4\u00b5\7(\2\2\u00b5*\3\2")
        buf.write("\2\2\u00b6\u00b7\7#\2\2\u00b7\u00b8\7?\2\2\u00b8,\3\2")
        buf.write("\2\2\u00b9\u00ba\7?\2\2\u00ba\u00bb\7?\2\2\u00bb.\3\2")
        buf.write("\2\2\u00bc\u00bd\7>\2\2\u00bd\60\3\2\2\2\u00be\u00bf\7")
        buf.write("@\2\2\u00bf\62\3\2\2\2\u00c0\u00c1\7>\2\2\u00c1\u00c2")
        buf.write("\7?\2\2\u00c2\64\3\2\2\2\u00c3\u00c4\7@\2\2\u00c4\u00c5")
        buf.write("\7?\2\2\u00c5\66\3\2\2\2\u00c6\u00c7\7?\2\2\u00c78\3\2")
        buf.write("\2\2\u00c8\u00c9\7*\2\2\u00c9:\3\2\2\2\u00ca\u00cb\7+")
        buf.write("\2\2\u00cb<\3\2\2\2\u00cc\u00cd\7}\2\2\u00cd>\3\2\2\2")
        buf.write("\u00ce\u00cf\7\177\2\2\u00cf@\3\2\2\2\u00d0\u00d1\7]\2")
        buf.write("\2\u00d1B\3\2\2\2\u00d2\u00d3\7_\2\2\u00d3D\3\2\2\2\u00d4")
        buf.write("\u00d5\7=\2\2\u00d5F\3\2\2\2\u00d6\u00d7\7.\2\2\u00d7")
        buf.write("H\3\2\2\2\u00d8\u00d9\7)\2\2\u00d9J\3\2\2\2\u00da\u00db")
        buf.write("\7d\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7m\2\2\u00dfL\3\2\2\2\u00e0\u00e2")
        buf.write("\t\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4N\3\2\2\2\u00e5")
        buf.write("\u00e7\t\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3")
        buf.write("\2\2\2\u00ea\u00ee\7\60\2\2\u00eb\u00ed\t\2\2\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef\u00fa\3\2\2\2\u00f0\u00ee\3")
        buf.write("\2\2\2\u00f1\u00f3\t\3\2\2\u00f2\u00f4\t\4\2\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5")
        buf.write("\u00f7\t\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3")
        buf.write("\2\2\2\u00fa\u00f1\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u0122")
        buf.write("\3\2\2\2\u00fc\u00fe\t\2\2\2\u00fd\u00fc\3\2\2\2\u00fe")
        buf.write("\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0104\7")
        buf.write("\60\2\2\u0103\u0105\t\2\2\2\u0104\u0103\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0107\u0111\3\2\2\2\u0108\u010a\t\3\2\2\u0109\u010b\t")
        buf.write("\4\2\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010d")
        buf.write("\3\2\2\2\u010c\u010e\t\2\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2")
        buf.write("\u0110\u0112\3\2\2\2\u0111\u0108\3\2\2\2\u0111\u0112\3")
        buf.write("\2\2\2\u0112\u0122\3\2\2\2\u0113\u0115\t\2\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a\t\3\2\2")
        buf.write("\u0119\u011b\t\4\2\2\u011a\u0119\3\2\2\2\u011a\u011b\3")
        buf.write("\2\2\2\u011b\u011d\3\2\2\2\u011c\u011e\t\2\2\2\u011d\u011c")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u011d\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u00e6\3\2\2\2")
        buf.write("\u0121\u00ff\3\2\2\2\u0121\u0114\3\2\2\2\u0122P\3\2\2")
        buf.write("\2\u0123\u0137\7$\2\2\u0124\u0125\7^\2\2\u0125\u0136\7")
        buf.write("d\2\2\u0126\u0127\7^\2\2\u0127\u0136\7h\2\2\u0128\u0129")
        buf.write("\7^\2\2\u0129\u0136\7t\2\2\u012a\u012b\7^\2\2\u012b\u0136")
        buf.write("\7p\2\2\u012c\u012d\7^\2\2\u012d\u0136\7v\2\2\u012e\u012f")
        buf.write("\7^\2\2\u012f\u0136\7$\2\2\u0130\u0131\7^\2\2\u0131\u0136")
        buf.write("\7^\2\2\u0132\u0133\7^\2\2\u0133\u0136\5I%\2\u0134\u0136")
        buf.write("\n\5\2\2\u0135\u0124\3\2\2\2\u0135\u0126\3\2\2\2\u0135")
        buf.write("\u0128\3\2\2\2\u0135\u012a\3\2\2\2\u0135\u012c\3\2\2\2")
        buf.write("\u0135\u012e\3\2\2\2\u0135\u0130\3\2\2\2\u0135\u0132\3")
        buf.write("\2\2\2\u0135\u0134\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u013a\u013b\7$\2\2\u013b\u013c\b)\2\2\u013c")
        buf.write("R\3\2\2\2\u013d\u013e\7v\2\2\u013e\u013f\7t\2\2\u013f")
        buf.write("\u0140\7w\2\2\u0140\u0147\7g\2\2\u0141\u0142\7h\2\2\u0142")
        buf.write("\u0143\7c\2\2\u0143\u0144\7n\2\2\u0144\u0145\7u\2\2\u0145")
        buf.write("\u0147\7g\2\2\u0146\u013d\3\2\2\2\u0146\u0141\3\2\2\2")
        buf.write("\u0147T\3\2\2\2\u0148\u0149\t\6\2\2\u0149\u014a\b+\3\2")
        buf.write("\u014aV\3\2\2\2\u014b\u0162\7$\2\2\u014c\u014d\7^\2\2")
        buf.write("\u014d\u0161\n\7\2\2\u014e\u014f\7^\2\2\u014f\u0161\7")
        buf.write("d\2\2\u0150\u0151\7^\2\2\u0151\u0161\7h\2\2\u0152\u0153")
        buf.write("\7^\2\2\u0153\u0161\7t\2\2\u0154\u0155\7^\2\2\u0155\u0161")
        buf.write("\7p\2\2\u0156\u0157\7^\2\2\u0157\u0161\7v\2\2\u0158\u0159")
        buf.write("\7^\2\2\u0159\u0161\5I%\2\u015a\u015b\7^\2\2\u015b\u0161")
        buf.write("\7$\2\2\u015c\u015d\7^\2\2\u015d\u0161\7^\2\2\u015e\u015f")
        buf.write("\7b\2\2\u015f\u0161\7)\2\2\u0160\u014c\3\2\2\2\u0160\u014e")
        buf.write("\3\2\2\2\u0160\u0150\3\2\2\2\u0160\u0152\3\2\2\2\u0160")
        buf.write("\u0154\3\2\2\2\u0160\u0156\3\2\2\2\u0160\u0158\3\2\2\2")
        buf.write("\u0160\u015a\3\2\2\2\u0160\u015c\3\2\2\2\u0160\u015e\3")
        buf.write("\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165")
        buf.write("\u0166\b,\4\2\u0166X\3\2\2\2\u0167\u017b\7$\2\2\u0168")
        buf.write("\u0169\7^\2\2\u0169\u017a\7d\2\2\u016a\u016b\7^\2\2\u016b")
        buf.write("\u017a\7h\2\2\u016c\u016d\7^\2\2\u016d\u017a\7t\2\2\u016e")
        buf.write("\u016f\7^\2\2\u016f\u017a\7p\2\2\u0170\u0171\7^\2\2\u0171")
        buf.write("\u017a\7v\2\2\u0172\u0173\7^\2\2\u0173\u017a\7$\2\2\u0174")
        buf.write("\u0175\7^\2\2\u0175\u017a\5I%\2\u0176\u0177\7^\2\2\u0177")
        buf.write("\u017a\7^\2\2\u0178\u017a\n\5\2\2\u0179\u0168\3\2\2\2")
        buf.write("\u0179\u016a\3\2\2\2\u0179\u016c\3\2\2\2\u0179\u016e\3")
        buf.write("\2\2\2\u0179\u0170\3\2\2\2\u0179\u0172\3\2\2\2\u0179\u0174")
        buf.write("\3\2\2\2\u0179\u0176\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017e\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\b")
        buf.write("-\5\2\u017fZ\3\2\2\2\u0180\u0181\7\61\2\2\u0181\u0182")
        buf.write("\7,\2\2\u0182\u0186\3\2\2\2\u0183\u0185\13\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0187\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0189\u018a\7,\2\2\u018a\u019b\7\61\2\2\u018b\u018c")
        buf.write("\7\61\2\2\u018c\u018d\7\61\2\2\u018d\u0191\3\2\2\2\u018e")
        buf.write("\u0190\n\b\2\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0197\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0194\u0196\13\2\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0197\u0195\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3")
        buf.write("\2\2\2\u019a\u0180\3\2\2\2\u019a\u018b\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c\u019d\b.\6\2\u019d\\\3\2\2\2\u019e\u01a0")
        buf.write("\t\t\2\2\u019f\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a4\b/\6\2\u01a4^\3\2\2\2\u01a5\u01a7\t\n\2\2")
        buf.write("\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ad\3\2\2\2\u01aa\u01ac")
        buf.write("\t\13\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae`\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2 \2\u00e3\u00e8\u00ee\u00f3\u00f8\u00fa")
        buf.write("\u00ff\u0106\u010a\u010f\u0111\u0116\u011a\u011f\u0121")
        buf.write("\u0135\u0137\u0146\u0160\u0162\u0179\u017b\u0186\u0191")
        buf.write("\u0197\u019a\u01a1\u01a8\u01ad\7\3)\2\3+\3\3,\4\3-\5\b")
        buf.write("\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    BOOLTYPE = 2
    VOIDTYPE = 3
    STRINGTYPE = 4
    FLOATTYPE = 5
    CONTINUE = 6
    ELSE = 7
    FOR = 8
    IF = 9
    RETURN = 10
    DO = 11
    WHILE = 12
    ADD = 13
    SUB = 14
    MUL = 15
    DIV = 16
    NOT = 17
    MOD = 18
    OR = 19
    AND = 20
    NEQ = 21
    EQ = 22
    LT = 23
    GT = 24
    LTEQ = 25
    GTEQ = 26
    ASSIGN = 27
    LP = 28
    RP = 29
    LB = 30
    RB = 31
    LS = 32
    RS = 33
    SEMI = 34
    COMMA = 35
    CA = 36
    BREAK = 37
    INTLIT = 38
    FLOATLIT = 39
    STRING_LIT = 40
    BOOLLIT = 41
    ERROR_CHAR = 42
    ILLEGAL_ESCAPE = 43
    UNCLOSE_STRING = 44
    CMT = 45
    WS = 46
    ID = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'boolean'", "'void'", "'string'", "'float'", "'continue'", 
            "'else'", "'for'", "'if'", "'return'", "'do'", "'while'", "'+'", 
            "'-'", "'*'", "'/'", "'!'", "'%'", "'||'", "'&&'", "'!='", "'=='", 
            "'<'", "'>'", "'<='", "'>='", "'='", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "'''", "'break'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "BOOLTYPE", "VOIDTYPE", "STRINGTYPE", "FLOATTYPE", 
            "CONTINUE", "ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", "ADD", 
            "SUB", "MUL", "DIV", "NOT", "MOD", "OR", "AND", "NEQ", "EQ", 
            "LT", "GT", "LTEQ", "GTEQ", "ASSIGN", "LP", "RP", "LB", "RB", 
            "LS", "RS", "SEMI", "COMMA", "CA", "BREAK", "INTLIT", "FLOATLIT", 
            "STRING_LIT", "BOOLLIT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "CMT", "WS", "ID" ]

    ruleNames = [ "INTTYPE", "BOOLTYPE", "VOIDTYPE", "STRINGTYPE", "FLOATTYPE", 
                  "CONTINUE", "ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", 
                  "ADD", "SUB", "MUL", "DIV", "NOT", "MOD", "OR", "AND", 
                  "NEQ", "EQ", "LT", "GT", "LTEQ", "GTEQ", "ASSIGN", "LP", 
                  "RP", "LB", "RB", "LS", "RS", "SEMI", "COMMA", "CA", "BREAK", 
                  "INTLIT", "FLOATLIT", "STRING_LIT", "BOOLLIT", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "CMT", "WS", "ID" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[39] = self.STRING_LIT_action 
            actions[41] = self.ERROR_CHAR_action 
            actions[42] = self.ILLEGAL_ESCAPE_action 
            actions[43] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                tmp = self.text;
                chieuDai = len(tmp) -1;
                self.text = tmp[1:chieuDai];

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise ErrorToken(self.text);

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:]);

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise UncloseString(self.text[1:]);

     


