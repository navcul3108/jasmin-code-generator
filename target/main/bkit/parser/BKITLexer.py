# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0235\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3")
        buf.write("\2\7\2\u00ab\n\2\f\2\16\2\u00ae\13\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\7\3\u00b6\n\3\f\3\16\3\u00b9\13\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4\u00c2\n\4\3\5\3\5\3\5\3\5\7\5\u00c8")
        buf.write("\n\5\f\5\16\5\u00cb\13\5\3\6\3\6\3\6\3\6\7\6\u00d1\n\6")
        buf.write("\f\6\16\6\u00d4\13\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\7\b\u00e0\n\b\f\b\16\b\u00e3\13\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00f0\n\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u010e\n\22\3\23\6\23\u0111\n\23\r")
        buf.write("\23\16\23\u0112\3\23\5\23\u0116\n\23\3\23\3\23\6\23\u011a")
        buf.write("\n\23\r\23\16\23\u011b\3\23\5\23\u011f\n\23\3\24\3\24")
        buf.write("\7\24\u0123\n\24\f\24\16\24\u0126\13\24\3\25\3\25\3\25")
        buf.write("\3\25\7\25\u012c\n\25\f\25\16\25\u012f\13\25\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u0135\n\26\f\26\16\26\u0138\13\26\3\27")
        buf.write("\3\27\7\27\u013c\n\27\f\27\16\27\u013f\13\27\3\30\3\30")
        buf.write("\5\30\u0143\n\30\3\30\6\30\u0146\n\30\r\30\16\30\u0147")
        buf.write("\3\31\3\31\5\31\u014c\n\31\3\32\3\32\7\32\u0150\n\32\f")
        buf.write("\32\16\32\u0153\13\32\3\33\3\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39\39\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3")
        buf.write("@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3C\3D\3D\3D\3D\3E\3E\3")
        buf.write("F\3F\3F\3G\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3")
        buf.write("N\3N\3O\3O\3P\3P\3Q\3Q\3R\6R\u022e\nR\rR\16R\u022f\3R")
        buf.write("\3R\3S\3S\3\u00d2\2T\3\3\5\4\7\2\t\5\13\6\r\2\17\7\21")
        buf.write("\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\b%\t\'\2)\2")
        buf.write("+\2-\2/\2\61\n\63\13\65\f\67\r9\16;\17=\20?\21A\22C\23")
        buf.write("E\24G\25I\26K\27M\30O\31Q\32S\33U\34W\35Y\36[\37] _!a")
        buf.write("\"c#e$g%i&k\'m(o)q*s+u,w-y.{/}\60\177\61\u0081\62\u0083")
        buf.write("\63\u0085\64\u0087\65\u0089\66\u008b\67\u008d8\u008f9")
        buf.write("\u0091:\u0093;\u0095<\u0097=\u0099>\u009b?\u009d@\u009f")
        buf.write("A\u00a1B\u00a3C\u00a5D\3\2\24\6\2\f\f$$))^^\b\2^^ddhh")
        buf.write("ppttvv\3\2$$\4\2\f\f))\3\2,,\3\2\62;\3\2\63;\4\2ZZzz\4")
        buf.write("\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\4\2GGgg\4\2")
        buf.write("--//\3\2c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0247\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\3\u00a7\3\2\2\2\5\u00b2\3\2\2")
        buf.write("\2\7\u00c1\3\2\2\2\t\u00c3\3\2\2\2\13\u00cc\3\2\2\2\r")
        buf.write("\u00d9\3\2\2\2\17\u00dc\3\2\2\2\21\u00ef\3\2\2\2\23\u00f1")
        buf.write("\3\2\2\2\25\u00f4\3\2\2\2\27\u00f7\3\2\2\2\31\u00fa\3")
        buf.write("\2\2\2\33\u00fd\3\2\2\2\35\u0100\3\2\2\2\37\u0103\3\2")
        buf.write("\2\2!\u0106\3\2\2\2#\u010d\3\2\2\2%\u011e\3\2\2\2\'\u0120")
        buf.write("\3\2\2\2)\u0127\3\2\2\2+\u0130\3\2\2\2-\u0139\3\2\2\2")
        buf.write("/\u0140\3\2\2\2\61\u014b\3\2\2\2\63\u014d\3\2\2\2\65\u0154")
        buf.write("\3\2\2\2\67\u0159\3\2\2\29\u015f\3\2\2\2;\u0168\3\2\2")
        buf.write("\2=\u016b\3\2\2\2?\u0172\3\2\2\2A\u017a\3\2\2\2C\u0180")
        buf.write("\3\2\2\2E\u0187\3\2\2\2G\u0190\3\2\2\2I\u0194\3\2\2\2")
        buf.write("K\u019d\3\2\2\2M\u01a2\3\2\2\2O\u01a5\3\2\2\2Q\u01af\3")
        buf.write("\2\2\2S\u01b6\3\2\2\2U\u01bb\3\2\2\2W\u01bf\3\2\2\2Y\u01c5")
        buf.write("\3\2\2\2[\u01ca\3\2\2\2]\u01d0\3\2\2\2_\u01d6\3\2\2\2")
        buf.write("a\u01d8\3\2\2\2c\u01da\3\2\2\2e\u01dc\3\2\2\2g\u01de\3")
        buf.write("\2\2\2i\u01e0\3\2\2\2k\u01e3\3\2\2\2m\u01e5\3\2\2\2o\u01e7")
        buf.write("\3\2\2\2q\u01ea\3\2\2\2s\u01ed\3\2\2\2u\u01ef\3\2\2\2")
        buf.write("w\u01f2\3\2\2\2y\u01f5\3\2\2\2{\u01f8\3\2\2\2}\u01fb\3")
        buf.write("\2\2\2\177\u01fe\3\2\2\2\u0081\u0202\3\2\2\2\u0083\u0205")
        buf.write("\3\2\2\2\u0085\u0208\3\2\2\2\u0087\u020c\3\2\2\2\u0089")
        buf.write("\u0210\3\2\2\2\u008b\u0212\3\2\2\2\u008d\u0215\3\2\2\2")
        buf.write("\u008f\u0218\3\2\2\2\u0091\u021a\3\2\2\2\u0093\u021c\3")
        buf.write("\2\2\2\u0095\u021e\3\2\2\2\u0097\u0220\3\2\2\2\u0099\u0222")
        buf.write("\3\2\2\2\u009b\u0224\3\2\2\2\u009d\u0226\3\2\2\2\u009f")
        buf.write("\u0228\3\2\2\2\u00a1\u022a\3\2\2\2\u00a3\u022d\3\2\2\2")
        buf.write("\u00a5\u0233\3\2\2\2\u00a7\u00ac\7$\2\2\u00a8\u00ab\5")
        buf.write("\21\t\2\u00a9\u00ab\n\2\2\2\u00aa\u00a8\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3")
        buf.write("\2\2\2\u00af\u00b0\5\7\4\2\u00b0\u00b1\b\2\2\2\u00b1\4")
        buf.write("\3\2\2\2\u00b2\u00b7\7$\2\2\u00b3\u00b6\5\21\t\2\u00b4")
        buf.write("\u00b6\n\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb")
        buf.write("\b\3\3\2\u00bb\6\3\2\2\2\u00bc\u00bd\7^\2\2\u00bd\u00c2")
        buf.write("\n\3\2\2\u00be\u00bf\7)\2\2\u00bf\u00c2\n\4\2\2\u00c0")
        buf.write("\u00c2\t\5\2\2\u00c1\u00bc\3\2\2\2\u00c1\u00be\3\2\2\2")
        buf.write("\u00c1\u00c0\3\2\2\2\u00c2\b\3\2\2\2\u00c3\u00c9\5\r\7")
        buf.write("\2\u00c4\u00c8\n\6\2\2\u00c5\u00c6\7,\2\2\u00c6\u00c8")
        buf.write("\n\6\2\2\u00c7\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8")
        buf.write("\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2")
        buf.write("\u00ca\n\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00d2\5\r\7")
        buf.write("\2\u00cd\u00d1\n\6\2\2\u00ce\u00cf\7,\2\2\u00cf\u00d1")
        buf.write("\n\6\2\2\u00d0\u00cd\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("\u00d4\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\5")
        buf.write("\r\7\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\b\6\4\2\u00d8\f")
        buf.write("\3\2\2\2\u00d9\u00da\7,\2\2\u00da\u00db\7,\2\2\u00db\16")
        buf.write("\3\2\2\2\u00dc\u00e1\7$\2\2\u00dd\u00e0\5\21\t\2\u00de")
        buf.write("\u00e0\n\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2")
        buf.write("\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3")
        buf.write("\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5")
        buf.write("\7$\2\2\u00e5\u00e6\b\b\5\2\u00e6\20\3\2\2\2\u00e7\u00f0")
        buf.write("\5\23\n\2\u00e8\u00f0\5\25\13\2\u00e9\u00f0\5\27\f\2\u00ea")
        buf.write("\u00f0\5\31\r\2\u00eb\u00f0\5\33\16\2\u00ec\u00f0\5\35")
        buf.write("\17\2\u00ed\u00f0\5\37\20\2\u00ee\u00f0\5!\21\2\u00ef")
        buf.write("\u00e7\3\2\2\2\u00ef\u00e8\3\2\2\2\u00ef\u00e9\3\2\2\2")
        buf.write("\u00ef\u00ea\3\2\2\2\u00ef\u00eb\3\2\2\2\u00ef\u00ec\3")
        buf.write("\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\22")
        buf.write("\3\2\2\2\u00f1\u00f2\7)\2\2\u00f2\u00f3\7$\2\2\u00f3\24")
        buf.write("\3\2\2\2\u00f4\u00f5\7^\2\2\u00f5\u00f6\7d\2\2\u00f6\26")
        buf.write("\3\2\2\2\u00f7\u00f8\7^\2\2\u00f8\u00f9\7h\2\2\u00f9\30")
        buf.write("\3\2\2\2\u00fa\u00fb\7^\2\2\u00fb\u00fc\7t\2\2\u00fc\32")
        buf.write("\3\2\2\2\u00fd\u00fe\7^\2\2\u00fe\u00ff\7p\2\2\u00ff\34")
        buf.write("\3\2\2\2\u0100\u0101\7^\2\2\u0101\u0102\7v\2\2\u0102\36")
        buf.write("\3\2\2\2\u0103\u0104\7^\2\2\u0104\u0105\7)\2\2\u0105 ")
        buf.write("\3\2\2\2\u0106\u0107\7^\2\2\u0107\u0108\7^\2\2\u0108\"")
        buf.write("\3\2\2\2\u0109\u010e\7\62\2\2\u010a\u010e\5\'\24\2\u010b")
        buf.write("\u010e\5)\25\2\u010c\u010e\5+\26\2\u010d\u0109\3\2\2\2")
        buf.write("\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c\3")
        buf.write("\2\2\2\u010e$\3\2\2\2\u010f\u0111\t\7\2\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0116\5-\27\2")
        buf.write("\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117\u011f\5/\30\2\u0118\u011a\t\7\2\2\u0119\u0118")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\5-\27\2")
        buf.write("\u011e\u0110\3\2\2\2\u011e\u0119\3\2\2\2\u011f&\3\2\2")
        buf.write("\2\u0120\u0124\t\b\2\2\u0121\u0123\t\7\2\2\u0122\u0121")
        buf.write("\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125(\3\2\2\2\u0126\u0124\3\2\2\2\u0127")
        buf.write("\u0128\7\62\2\2\u0128\u0129\t\t\2\2\u0129\u012d\t\n\2")
        buf.write("\2\u012a\u012c\t\13\2\2\u012b\u012a\3\2\2\2\u012c\u012f")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("*\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131\7\62\2\2\u0131")
        buf.write("\u0132\t\f\2\2\u0132\u0136\t\r\2\2\u0133\u0135\t\16\2")
        buf.write("\2\u0134\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137,\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0139\u013d\7\60\2\2\u013a\u013c\t\7\2\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e.\3\2\2\2\u013f\u013d\3\2\2")
        buf.write("\2\u0140\u0142\t\17\2\2\u0141\u0143\t\20\2\2\u0142\u0141")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0146\t\7\2\2\u0145\u0144\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\60\3\2")
        buf.write("\2\2\u0149\u014c\5Y-\2\u014a\u014c\5[.\2\u014b\u0149\3")
        buf.write("\2\2\2\u014b\u014a\3\2\2\2\u014c\62\3\2\2\2\u014d\u0151")
        buf.write("\t\21\2\2\u014e\u0150\t\22\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\64\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0155\7D\2")
        buf.write("\2\u0155\u0156\7q\2\2\u0156\u0157\7f\2\2\u0157\u0158\7")
        buf.write("{\2\2\u0158\66\3\2\2\2\u0159\u015a\7D\2\2\u015a\u015b")
        buf.write("\7t\2\2\u015b\u015c\7g\2\2\u015c\u015d\7c\2\2\u015d\u015e")
        buf.write("\7m\2\2\u015e8\3\2\2\2\u015f\u0160\7E\2\2\u0160\u0161")
        buf.write("\7q\2\2\u0161\u0162\7p\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7k\2\2\u0164\u0165\7p\2\2\u0165\u0166\7w\2\2\u0166\u0167")
        buf.write("\7g\2\2\u0167:\3\2\2\2\u0168\u0169\7F\2\2\u0169\u016a")
        buf.write("\7q\2\2\u016a<\3\2\2\2\u016b\u016c\7G\2\2\u016c\u016d")
        buf.write("\7n\2\2\u016d\u016e\7u\2\2\u016e\u016f\7g\2\2\u016f\u0170")
        buf.write("\7K\2\2\u0170\u0171\7h\2\2\u0171>\3\2\2\2\u0172\u0173")
        buf.write("\7G\2\2\u0173\u0174\7p\2\2\u0174\u0175\7f\2\2\u0175\u0176")
        buf.write("\7D\2\2\u0176\u0177\7q\2\2\u0177\u0178\7f\2\2\u0178\u0179")
        buf.write("\7{\2\2\u0179@\3\2\2\2\u017a\u017b\7G\2\2\u017b\u017c")
        buf.write("\7p\2\2\u017c\u017d\7f\2\2\u017d\u017e\7K\2\2\u017e\u017f")
        buf.write("\7h\2\2\u017fB\3\2\2\2\u0180\u0181\7G\2\2\u0181\u0182")
        buf.write("\7p\2\2\u0182\u0183\7f\2\2\u0183\u0184\7H\2\2\u0184\u0185")
        buf.write("\7q\2\2\u0185\u0186\7t\2\2\u0186D\3\2\2\2\u0187\u0188")
        buf.write("\7G\2\2\u0188\u0189\7p\2\2\u0189\u018a\7f\2\2\u018a\u018b")
        buf.write("\7Y\2\2\u018b\u018c\7j\2\2\u018c\u018d\7k\2\2\u018d\u018e")
        buf.write("\7n\2\2\u018e\u018f\7g\2\2\u018fF\3\2\2\2\u0190\u0191")
        buf.write("\7H\2\2\u0191\u0192\7q\2\2\u0192\u0193\7t\2\2\u0193H\3")
        buf.write("\2\2\2\u0194\u0195\7H\2\2\u0195\u0196\7w\2\2\u0196\u0197")
        buf.write("\7p\2\2\u0197\u0198\7e\2\2\u0198\u0199\7v\2\2\u0199\u019a")
        buf.write("\7k\2\2\u019a\u019b\7q\2\2\u019b\u019c\7p\2\2\u019cJ\3")
        buf.write("\2\2\2\u019d\u019e\7G\2\2\u019e\u019f\7n\2\2\u019f\u01a0")
        buf.write("\7u\2\2\u01a0\u01a1\7g\2\2\u01a1L\3\2\2\2\u01a2\u01a3")
        buf.write("\7K\2\2\u01a3\u01a4\7h\2\2\u01a4N\3\2\2\2\u01a5\u01a6")
        buf.write("\7R\2\2\u01a6\u01a7\7c\2\2\u01a7\u01a8\7t\2\2\u01a8\u01a9")
        buf.write("\7c\2\2\u01a9\u01aa\7o\2\2\u01aa\u01ab\7g\2\2\u01ab\u01ac")
        buf.write("\7v\2\2\u01ac\u01ad\7g\2\2\u01ad\u01ae\7t\2\2\u01aeP\3")
        buf.write("\2\2\2\u01af\u01b0\7T\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2")
        buf.write("\7v\2\2\u01b2\u01b3\7w\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5")
        buf.write("\7p\2\2\u01b5R\3\2\2\2\u01b6\u01b7\7V\2\2\u01b7\u01b8")
        buf.write("\7j\2\2\u01b8\u01b9\7g\2\2\u01b9\u01ba\7p\2\2\u01baT\3")
        buf.write("\2\2\2\u01bb\u01bc\7X\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be")
        buf.write("\7t\2\2\u01beV\3\2\2\2\u01bf\u01c0\7Y\2\2\u01c0\u01c1")
        buf.write("\7j\2\2\u01c1\u01c2\7k\2\2\u01c2\u01c3\7n\2\2\u01c3\u01c4")
        buf.write("\7g\2\2\u01c4X\3\2\2\2\u01c5\u01c6\7V\2\2\u01c6\u01c7")
        buf.write("\7t\2\2\u01c7\u01c8\7w\2\2\u01c8\u01c9\7g\2\2\u01c9Z\3")
        buf.write("\2\2\2\u01ca\u01cb\7H\2\2\u01cb\u01cc\7c\2\2\u01cc\u01cd")
        buf.write("\7n\2\2\u01cd\u01ce\7u\2\2\u01ce\u01cf\7g\2\2\u01cf\\")
        buf.write("\3\2\2\2\u01d0\u01d1\7G\2\2\u01d1\u01d2\7p\2\2\u01d2\u01d3")
        buf.write("\7f\2\2\u01d3\u01d4\7F\2\2\u01d4\u01d5\7q\2\2\u01d5^\3")
        buf.write("\2\2\2\u01d6\u01d7\7-\2\2\u01d7`\3\2\2\2\u01d8\u01d9\7")
        buf.write("/\2\2\u01d9b\3\2\2\2\u01da\u01db\7,\2\2\u01dbd\3\2\2\2")
        buf.write("\u01dc\u01dd\7^\2\2\u01ddf\3\2\2\2\u01de\u01df\7\'\2\2")
        buf.write("\u01dfh\3\2\2\2\u01e0\u01e1\7#\2\2\u01e1\u01e2\7?\2\2")
        buf.write("\u01e2j\3\2\2\2\u01e3\u01e4\7>\2\2\u01e4l\3\2\2\2\u01e5")
        buf.write("\u01e6\7@\2\2\u01e6n\3\2\2\2\u01e7\u01e8\7>\2\2\u01e8")
        buf.write("\u01e9\7?\2\2\u01e9p\3\2\2\2\u01ea\u01eb\7@\2\2\u01eb")
        buf.write("\u01ec\7?\2\2\u01ecr\3\2\2\2\u01ed\u01ee\7?\2\2\u01ee")
        buf.write("t\3\2\2\2\u01ef\u01f0\7?\2\2\u01f0\u01f1\7?\2\2\u01f1")
        buf.write("v\3\2\2\2\u01f2\u01f3\7-\2\2\u01f3\u01f4\7\60\2\2\u01f4")
        buf.write("x\3\2\2\2\u01f5\u01f6\7/\2\2\u01f6\u01f7\7\60\2\2\u01f7")
        buf.write("z\3\2\2\2\u01f8\u01f9\7,\2\2\u01f9\u01fa\7\60\2\2\u01fa")
        buf.write("|\3\2\2\2\u01fb\u01fc\7^\2\2\u01fc\u01fd\7\60\2\2\u01fd")
        buf.write("~\3\2\2\2\u01fe\u01ff\7?\2\2\u01ff\u0200\7\61\2\2\u0200")
        buf.write("\u0201\7?\2\2\u0201\u0080\3\2\2\2\u0202\u0203\7>\2\2\u0203")
        buf.write("\u0204\7\60\2\2\u0204\u0082\3\2\2\2\u0205\u0206\7@\2\2")
        buf.write("\u0206\u0207\7\60\2\2\u0207\u0084\3\2\2\2\u0208\u0209")
        buf.write("\7>\2\2\u0209\u020a\7?\2\2\u020a\u020b\7\60\2\2\u020b")
        buf.write("\u0086\3\2\2\2\u020c\u020d\7@\2\2\u020d\u020e\7?\2\2\u020e")
        buf.write("\u020f\7\60\2\2\u020f\u0088\3\2\2\2\u0210\u0211\7#\2\2")
        buf.write("\u0211\u008a\3\2\2\2\u0212\u0213\7(\2\2\u0213\u0214\7")
        buf.write("(\2\2\u0214\u008c\3\2\2\2\u0215\u0216\7~\2\2\u0216\u0217")
        buf.write("\7~\2\2\u0217\u008e\3\2\2\2\u0218\u0219\7}\2\2\u0219\u0090")
        buf.write("\3\2\2\2\u021a\u021b\7\177\2\2\u021b\u0092\3\2\2\2\u021c")
        buf.write("\u021d\7]\2\2\u021d\u0094\3\2\2\2\u021e\u021f\7_\2\2\u021f")
        buf.write("\u0096\3\2\2\2\u0220\u0221\7<\2\2\u0221\u0098\3\2\2\2")
        buf.write("\u0222\u0223\7\60\2\2\u0223\u009a\3\2\2\2\u0224\u0225")
        buf.write("\7.\2\2\u0225\u009c\3\2\2\2\u0226\u0227\7=\2\2\u0227\u009e")
        buf.write("\3\2\2\2\u0228\u0229\7*\2\2\u0229\u00a0\3\2\2\2\u022a")
        buf.write("\u022b\7+\2\2\u022b\u00a2\3\2\2\2\u022c\u022e\t\23\2\2")
        buf.write("\u022d\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u022d\3")
        buf.write("\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232")
        buf.write("\bR\4\2\u0232\u00a4\3\2\2\2\u0233\u0234\13\2\2\2\u0234")
        buf.write("\u00a6\3\2\2\2\35\2\u00aa\u00ac\u00b5\u00b7\u00c1\u00c7")
        buf.write("\u00c9\u00d0\u00d2\u00df\u00e1\u00ef\u010d\u0112\u0115")
        buf.write("\u011b\u011e\u0124\u012d\u0136\u013d\u0142\u0147\u014b")
        buf.write("\u0151\u022f\6\3\2\2\3\3\3\b\2\2\3\b\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ILLEGAL_ESCAPE = 1
    UNCLOSE_STRING = 2
    UNTERMINATED_COMMENT = 3
    Comment = 4
    StrLit = 5
    IntLit = 6
    FloatLit = 7
    BoolLit = 8
    ID = 9
    BODY = 10
    BREAK = 11
    CONTINUE = 12
    DO = 13
    ELSEIF = 14
    ENDBODY = 15
    ENDIF = 16
    ENDFOR = 17
    ENDWHILE = 18
    FOR = 19
    FUNCTION = 20
    ELSE = 21
    IF = 22
    PARAMETER = 23
    RETURN = 24
    THEN = 25
    VAR = 26
    WHILE = 27
    TRUE = 28
    FALSE = 29
    ENDDO = 30
    ADD = 31
    SUB = 32
    MUL = 33
    DIV = 34
    MOD = 35
    NEQ = 36
    ST = 37
    GT = 38
    SE = 39
    GE = 40
    ASSIGN = 41
    EQ = 42
    ADDF = 43
    SUBF = 44
    MULF = 45
    DIVF = 46
    NEQF = 47
    STF = 48
    GTF = 49
    SEF = 50
    GEF = 51
    NOT = 52
    AND = 53
    OR = 54
    LB = 55
    RB = 56
    LS = 57
    RS = 58
    CL = 59
    DOT = 60
    CM = 61
    SC = 62
    LP = 63
    RP = 64
    WS = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'ElseIf'", "'EndBody'", 
            "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'Else'", "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", 
            "'While'", "'True'", "'False'", "'EndDo'", "'+'", "'-'", "'*'", 
            "'\\'", "'%'", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
            "'=='", "'+.'", "'-.'", "'*.'", "'\\.'", "'=/='", "'<.'", "'>.'", 
            "'<=.'", "'>=.'", "'!'", "'&&'", "'||'", "'{'", "'}'", "'['", 
            "']'", "':'", "'.'", "','", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "Comment", "StrLit", "IntLit", "FloatLit", "BoolLit", "ID", 
            "BODY", "BREAK", "CONTINUE", "DO", "ELSEIF", "ENDBODY", "ENDIF", 
            "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "ELSE", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NEQ", "ST", "GT", "SE", 
            "GE", "ASSIGN", "EQ", "ADDF", "SUBF", "MULF", "DIVF", "NEQF", 
            "STF", "GTF", "SEF", "GEF", "NOT", "AND", "OR", "LB", "RB", 
            "LS", "RS", "CL", "DOT", "CM", "SC", "LP", "RP", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ILLEGAL_CHAR", "UNTERMINATED_COMMENT", 
                  "Comment", "CMTSIG", "StrLit", "Escape", "DBLQUOINSIDE", 
                  "BACKSPACE", "FORMFEED", "CARRIAGE", "NEWLINE", "TAB", 
                  "SINGLEQUO", "BACKSLASH", "IntLit", "FloatLit", "INTEGER", 
                  "HEX", "OCT", "DEC", "EXP", "BoolLit", "ID", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "ELSE", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NEQ", "ST", "GT", 
                  "SE", "GE", "ASSIGN", "EQ", "ADDF", "SUBF", "MULF", "DIVF", 
                  "NEQF", "STF", "GTF", "SEF", "GEF", "NOT", "AND", "OR", 
                  "LB", "RB", "LS", "RS", "CL", "DOT", "CM", "SC", "LP", 
                  "RP", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.ILLEGAL_ESCAPE_action 
            actions[1] = self.UNCLOSE_STRING_action 
            actions[6] = self.StrLit_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]
     

    def StrLit_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     


