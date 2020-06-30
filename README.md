# Evaluation-of-QOE-through-Trace-Driven-Emulation

<b><h2>Introduction</b></h2>:
<p>                           Providing best user experience for video on demand services is possible by quantifying users’ experience using QOE metrics. Depending on the type of measurement, QOE metrics can be classified as subjective and objective metrics. Measurement of subjective QOE metrics is influenced by psychological factors of the user, and hence is biased and varies from one user to another, making it tedious and hard to measure.</p>

Earlier research works measured objective metrics like playback start time, number of interruptions, average bitrate, etc. But neither did they conduct experiment in real time network conditions nor did they consider different bandwidths patterns(consisting of both long and short bandwidth variations). This work proposes a real time trace driven emulation testbed to evaluate objective QOE metrics. The aim of this work is two fold: to create an emulation testbed capable of replicating wide–range network conditions using real time bandwidth traces and to do an extensive analysis of different rate adaptation algorithms for dash by choosing noteworthy QOE metrics under different real-time trace driven network conditions.

QOE Metrics:
Traditional QOS Metrics are not sufficient to quantify users’ experience.
Based on measurement methodologies, QOE metrics are either subjective metrics or objective metrics.
Playback start time, number of interruptions, quality of video file are some of objective metrics.
Mean Opinion Score is an example of subjective metrics. Subjective metrics are affected by psychological and physical factors.
Subjective QOE metrics are user-biased whereas objective QOE metrics can be automated. 
In this work, we consider number of bitrate switching events, number of re-buffering events, startup delay, time taken to reach highest bitrate and average bitrate perceived as objective QOE metrics for evaluation.

Throttling tool:
We used Linux Traffic Control(TC) as our throttling tool.
TC uses Token Bucket Filter(TBF) to throttle bandwidth of the link.
Traffic is filtered based on the expenditure of tokens.
Tokens roughly correspond to bytes and tokens arrive at a steady rate until bucket is full.
Of all other tools, we found TC convenient at the bandwidth range we are working.
