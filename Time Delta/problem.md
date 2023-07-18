# Problem

When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

> Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is 
to print the absolute difference (in seconds) between them.

**Input Format**

The first line contains $T$, the number of testcases.
Each testcase contains $2$ lines, representing time $t_1$ and time $t_2$ .

Constraints

- Input contains only valid timestamps
- $year \le 3000$

**Output Format**

Print the absolute difference $(t_1 - t_2)$ in seconds.