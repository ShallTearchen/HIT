 ..\..\crf_learn -t -c 4.0 template1 train1.data model2
 ..\..\crf_test -m model2 test1.data -o result2
perl conlleval.pl -d "	" <result2 >result2.info

