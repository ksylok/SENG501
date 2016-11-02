#!/bin/bash

i="1"
k="1"
GRAPH_OUTPUT="GRAPH_OUTPUT.txt"

if [ $i -eq 1 ]
then
hadoop jar /home/instructor/hadoop-streaming/hadoop-streaming-2.7.3.jar \
-D stream.map.output.field.separator="|" -D stream.num.map.output.key.fields=5 \
-D map.output.key.field.separator="|" -D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=5 -files graph_map.py,graph_red.py \
-mapper graph_map.py -reducer graph_red.py \
-input /user/ksylok/inputFiles/graph.txt -output /user/ksylok/graph/output_g$k \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
> $GRAPH_OUTPUT 2>&1
echo $GRAPH_OUTPUT
greyNodes=$(cat $GRAPH_OUTPUT | grep greyNodes | cut -d '=' -f 2)
echo $greyNodes
i=$[$i-1]
fi

while [ $greyNodes -gt 0 ]
do
hadoop jar /home/instructor/hadoop-streaming/hadoop-streaming-2.7.3.jar \
-D stream.map.output.field.separator="|" -D stream.num.map.output.key.fields=5 \
-D map.output.key.field.separator="|" -D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=5 -files graph_map.py,graph_red.py \
-mapper graph_map.py -reducer graph_red.py \
-input /user/ksylok/graph/output_g$k -output /user/ksylok/graph/output_g$[$k+1] \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
> $GRAPH_OUTPUT 2>&1
echo $GRAPH_OUTPUT
greyNodes=$(cat $GRAPH_OUTPUT | grep greyNodes | cut -d '=' -f 2)
echo $greyNodes
k=$[$k+1]
done
