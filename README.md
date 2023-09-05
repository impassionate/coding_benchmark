# coding_benchmark

A benchmark with 100 GPT_Generated python coding problems (mostly closely related to reeal life) with a specific grading standard that can be used to assess a generative AI's coding abilities in different aspects. <br />
The coding problems are divided into 4 parts: <br />1. Error/Edge cases handling; <br />2. Task Planning Ability; <br />3. Optimization Ability; <br />4. Regular General Test. <br />
Each part is divided into 3 levels of difficulties (easy-beginner level; medium-intermediate level; hard-expert level)



## What we are assessing using this benchmark?

- Error/Edge cases handling: used mainly to test if the AI can thoroughly handle all edge cases and error inputs
- Task Planning: In this section, we are focusing on testing if the AI has the ability to plan a certain task inreal life
- Optimization: Testing if the AI can optimize an algorithm/find a better solution based on a solution given. This is also useful in real-life scenario
- General Coding Test: Similar to Leetcode, we still need to do some traditional problems to test the overall coding ability in general<br />
With all these differents sections of tests, we will be able to get an overview of the generative AI's 'pentagon skill map' of its coding abilities. We might be able to compare 2 AI if one is better in some of the sections and overall who might have a better performance. Also as we involove assessment on Tasking Planning and Optimization, and the problems are closely related to real life, we are able to get a sense of the AI's ability to solve real-life problems and take its advantage (maybe some AIs are good at planning tasks but some are not).

## How it works

- These 100 problems compose a 'problem set' in which there are 1/3 easy problems, 1/3 medium, and 1/3 hard
- Ideally, we can use maybe automated tools like chatgpt to randomly choose several medium level problems in each section and grade the AI's solution with the grading standard in the benchmark doc file.Then give instruction that if th AI does well in this level (e.g, get a grade of 80+), for the next round, we will give it hard level problems in the sections it does well. This is similar to the dynamic adjustment of difficulty in GRE test and we may use the same / or similar mechanism. In addition, we will add a coefficient to different levels, for example, the final grade of a certain section (one aspect of the AI's coding ability) is 1*easy grade + 2*medium grade + 3*hard grade. This kind of mechanism may let us get a relatively reasonable result with the least number of problems for the AI to do, which is effective.<br />
- Currently, the data with so-called 'ground-truth' label is not easy to get as we are using more of real-life cases instead of leetcode problems, which has official 'optimal answers' and myriads of datasets to learn. However, we might ask software engineers in different levels to do these problems and adjust the overall rubric, and then let different AI repeat doing the problems and grade the solutions provided by themselves as well as developers to further improve the mechanism.
- The ground truth matters because it can serve as a basic standard; however, it might not be necessary since for novel things, there might be some break throughs that do not fit with the traditional pattern perfectly. And the 'ground truth' data for us might be collected using a large number of tries. (just like the ground truth data for leetcode is collected frome millions of users and countless tries)

-https://chat.openai.com/share/576d5e4a-ddd1-4daf-8345-977a8898d425    here is the link to gpt chatbox that shows how chatgpt4 does the automated assessments
