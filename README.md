# PRELIMINARY-ANALYSIS-ON-GPT-3.5-CAPABILITY

**Abstract**

Understanding sentiments and politeness in developer comments is essential for effective team dynamics and successful project outcomes in a software development context. This study utilizes the Generative Pretrained Transformer model (GPT-3.5) text-DaVinci-003 to analyze 13,645 developer comments from the Zookeeper project, part of the Apache ecosystem.

1. Research Aims and Objectives

Given these challenges, this research aims to evaluate the Generative Pre-trained Transformer (GPT-3.5) text-davinci-003 model in the sentiment and politeness analysis of developer comments from the Zookeeper project. It is part of the Jira issue tracking system of the Apache ecosystem. The objectives are as follows: We seek to extend the existing research by using the GPT-3.5 model as a unified tool for both sentiment and politeness analysis, while also providing a more nuanced understanding by including a neutral category in the sentiment analysis. To enhance the interpretability of results, add confidence level and reasoning for every classification by the model.

1.2 Research Questions

RQ1. How does the GPT-3.5 text-davinci-003 model perform on politeness analysis?
RQ2. How does the GPT-3.5 text-davinci-003 model perform on sentiment analysis?

1.3 Research Approach

We've proposed a multi-phase study approach to accomplish our primary goal, which is to evaluate the capabilities and limitations of the GPT-3.5 model in categorizing politeness and sentiment in developers' comments. We start by extracting a large dataset from the Apache Zookeeper project, providing us with a robust platform for analysis.
Our methodology is designed to critically evaluate the model's performance in comparison to both existing benchmarks and human annotators. We use a range of evaluation metrics, including Cohen's Kappa, accuracy, recall, and F1-score, to provide a detailed insight of the model's performance. Our research is divided into key phases, each focusing on a specific research question, allowing us to accomplish our measurable goals methodically. This structured approach ensures that our findings are both reliable and applicable to real-world scenarios.

2. Data Source
   
For our research, we focused on one specific project within the Apache ecosystem: the Zookeeper project. It consists of 13,645 comments in the database and the involvement of 495 developers. We chose Apache because it's a widely researched software ecosystem and more specifically the Zookeeper project. The data of this project has a wide range of comment lengths, it provides a solid evaluation of the GPT-3.5 model's performance across a range of comment sizes. This selection allows us to generalise our conclusions to similar open-source ecosystem projects. To align with our research objectives, we extracted columns such as project_name, comment, sentiment, and politeness. The dataset is uploaded in
Kaggle:https://www.kaggle.com/datasets/hasithakutala/preliminary-analysis-on-gpt-35-capability?select=ZooKeeper_Project_Dataset.xlsx


