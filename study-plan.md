# 📊 12-Month Data Science + Machine Learning Engineering Study Plan

**Duration:** 12 months (52 weeks)\
**Study time:** 8--12 hours per week\
**Current starting point:** Advanced Python; comfortable with
NumPy/Pandas; basic SQL; beginner ML; mathematics and statistics need
revision\
**Learning style:** Balanced theory, concise notes, exercises, projects,
and assessment\
**Resources:** Free-first\
**Career goals:** Data Science and Machine Learning Engineering\
**Additional goal:** Prepare a strong academic and technical profile for
a master's degree abroad

> [!NOTE]
> **Professional dashboard view:** This plan keeps a fixed weekly cadence, milestone checks, and project-based evidence of progress across Data Science and ML Engineering.

| 📌 Plan Snapshot | Value |
|---|---|
| **Duration** | 12 months (52 weeks) |
| **Weekly Study Time** | 8--12 hours |
| **Primary Track** | Data Science + Machine Learning Engineering |
| **Outcome Focus** | Reproducible projects, evaluation rigor, and portfolio readiness |

### 🧭 Quick Navigation
- [📘 Plan Overview](#-1-plan-overview)
- [🗓️ Fixed Weekly Timetable](#️-2-fixed-weekly-timetable)
- [🗺️ Detailed 52-Week Curriculum](#️-3-detailed-52-week-curriculum)
- [📝 Notes and Revision System](#-4-notes-and-revision-system)
- [✅ Exercise Levels and Answer Checks](#-5-exercise-levels-and-answer-checks)
- [🧱 Portfolio Projects](#-6-portfolio-projects)
- [📚 Free Learning Resource Library](#-7-free-learning-resource-library)
- [🎯 Monthly Milestone Checklist](#-8-monthly-milestone-checklist)
- [🎓 Master's Abroad Preparation](#-9-masters-abroad-preparation)
- [📜 Rules for the Year](#-10-rules-for-the-year)

---
## 📘 1. Plan Overview

The plan develops two complementary skill sets:

-   **Data Science:** data cleaning, SQL, statistics, exploratory
    analysis, visualization, machine learning, interpretation, and
    communication.
-   **Machine Learning Engineering:** reproducible pipelines, testing,
    APIs, containers, experiment tracking, and deployment fundamentals.

The first half emphasizes foundations. The second half moves toward
applied projects and engineering. Deep learning, Spark, Kubernetes,
advanced cloud infrastructure, and complex MLOps are optional
extensions---not prerequisites for completing this plan.

### 🧭 Twelve-month roadmap

| Month | Main focus | Expected deliverable |
|---|---|---|
| 1 | NumPy, Pandas, data cleaning, Git | Clean dataset and analysis notebook |
| 2 | SQL, EDA, visualization | EDA report with useful findings |
| 3 | Probability, descriptive statistics, distributions | Simulation exercises and formula notes |
| 4 | Inference, hypothesis testing, experiments | Statistical investigation report |
| 5 | ML workflow, regression, preprocessing | Reproducible regression project |
| 6 | Classification, trees, ensembles, evaluation | Classification project with fair model comparison |
| 7 | Advanced SQL, feature engineering, clustering, PCA | Segmentation or unsupervised-learning study |
| 8 | Explainability, dashboards, data storytelling | Interactive dashboard and report |
| 9 | Software engineering, tests, APIs, Docker | Tested prediction API |
| 10 | MLflow, CI, deployment and monitoring concepts | Reproducible model service |
| 11 | Capstone proposal and implementation | End-to-end capstone |
| 12 | Portfolio polish, revision, graduate-school preparation | Published portfolio and application checklist |

---
## 🗓️ 2. Fixed Weekly Timetable

This default schedule provides **9 planned hours per week**, leaving
1--3 flexible hours for difficult topics, extra project work, or
university deadlines.

| Day | Time | Activity |
|---|---:|---|
| Monday | 1 hour | Learn concepts and write concise notes |
| Tuesday | 1.5 hours | Guided coding and reproduce key examples |
| Wednesday | 1 hour | Math, SQL, or problem-solving practice |
| Thursday | 1.5 hours | Independent exercises without looking at solutions first |
| Saturday | 3 hours | Project development using the week's concepts |
| Sunday | 1 hour | Quiz, error correction, revision, and planning |

### 🔁 Weekly learning loop

1.  Read or watch one focused lesson.
2.  Write short notes in your own words.
3.  Reproduce a small example.
4.  Solve an independent exercise.
5.  Apply the concept to a dataset or project.
6.  Check the answer and explain any errors.
7.  Commit meaningful work to Git.

During university exams, use a reduced maintenance schedule rather than
attempting to catch up on everything at once.

---
# 🗺️ 3. Detailed 52-Week Curriculum

> [!TIP]
> **How to use this roadmap:** Treat each week as a deliverable unit—complete the exercises, perform the answer checks, and only then move forward.

## 🟦 Month 1 — NumPy, Pandas, and Data Quality

**Goal:** Transform unfamiliar datasets reliably and explain
data-cleaning decisions.

### 📅 Week 1 — NumPy arrays and vectorization

**Topics and concepts** - Arrays, dimensions, shapes, dtypes, indexing -
Vectorized calculations versus Python loops - Broadcasting rules and
aggregation - Basic numerical precision

**Notes to prepare** - What `shape`, `ndim`, and `dtype` mean -
Broadcasting compatibility rules - Two worked examples of vectorized
operations

**Exercises** 1. Create one-dimensional and two-dimensional arrays. 2.
Calculate row-wise and column-wise summaries. 3. Normalize a numerical
array. 4. Predict the result of several broadcasting operations before
running them.

**Answer checks** - Check shapes before performing operations. - Explain
why dimensions are compatible or incompatible. - Compare numerical
outputs with a small hand calculation.

**Weekly deliverable:** a notebook of array exercises with explanations.

### 📅 Week 2 — NumPy indexing and array operations

**Topics and concepts** - Slicing, Boolean masks, fancy indexing -
`where`, `argsort`, `argmax`, `argmin`, `nonzero` - `take`, `put`,
`diag`, `triu`, `tril`, `clip` - Sorting and aggregation

**Exercises** 1. Filter rows that satisfy multiple conditions. 2. Find
the index of the largest value in each row. 3. Sort records by a
selected feature. 4. Clip values to a valid range. 5. Extract triangular
and diagonal portions of a matrix.

**Answer checks** - Test with a small array whose correct output can be
calculated manually. - Verify whether indexing returns a view or a copy
where relevant. - Check boundary cases and ties.

**Weekly deliverable:** a compact NumPy exercise notebook.

### 📅 Week 3 — Pandas manipulation

**Topics and concepts** - Series and DataFrames - Selection, filtering,
sorting - `groupby`, `agg`, `transform` - `merge`, concatenation,
reshaping - Date and categorical data

**Exercises** 1. Answer ten questions about a tabular dataset. 2. Group
records and calculate multiple summary statistics. 3. Join two tables
using keys. 4. Compare aggregate results before and after a join.

**Answer checks** - Verify row counts and join cardinality. - Check
totals against independent calculations. - Explain the difference
between grouped aggregation and row-preserving transformation.

**Weekly deliverable:** a notebook answering ten data questions.

### 📅 Week 4 — Data cleaning and Git

**Topics and concepts** - Missing values, duplicates, inconsistent
categories - Type conversion and date parsing - Outlier investigation -
Tidy data and data dictionaries - Git commits and README basics

**Exercises** 1. Audit a dataset before cleaning. 2. Document
missingness and duplicates. 3. Clean types and inconsistent categories.
4. Write a data-quality report explaining each decision.

**Answer checks** - Compare data-quality counts before and after
cleaning. - Do not delete outliers automatically; investigate whether
they are errors or valid observations. - Ensure cleaning decisions are
reproducible.

**Dataset:** [Palmer
Penguins](https://allisonhorst.github.io/palmerpenguins/) or [UCI
Adult](https://archive.ics.uci.edu/dataset/2/adult).

**Month 1 milestone:** clean a dataset and explain the steps from raw
data to analysis-ready data.

---
## 🟦 Month 2 — SQL, EDA, and Visualization

**Goal:** Query datasets independently and communicate findings clearly.

### 📅 Week 5 — SQL fundamentals

**Topics and concepts** - `SELECT`, `WHERE`, `CASE`, `ORDER BY` - `NULL`
and three-valued logic - Aggregation, `GROUP BY`, `HAVING` - Filtering
before and after aggregation

**Exercises** - Complete at least 15 SQL questions. - Group records by
category and calculate totals. - Find top categories and date ranges. -
Practice conditions involving missing values.

**Answer checks** - Verify filtering order and aggregate logic. - Check
`NULL` handling explicitly. - Test queries on a small hand-checkable
table.

### 📅 Week 6 — Joins, subqueries, and CTEs

**Topics and concepts** - Inner and left joins - Primary and foreign
keys - Subqueries and common table expressions - Date functions -
Duplicate rows caused by joins

**Exercises** - Solve ten multi-table analytical questions. - Find
records without matching references. - Calculate category-level metrics
across tables.

**Answer checks** - Check whether joins multiply records. - Confirm
unmatched rows are retained when required. - Compare counts before and
after joining.

**Resource:** [SQLBolt](https://sqlbolt.com/).

### 📅 Week 7 — Exploratory data analysis

**Topics and concepts** - Univariate and bivariate analysis - Numerical
and categorical variables - Distributions, outliers, and missingness -
Group comparisons - Correlation and its limitations

**Exercises** - Investigate five numerical and three categorical
variables. - Create plots that answer specific questions. - Record
surprising results and possible explanations.

**Answer checks** - Distinguish observations from interpretations. - Do
not infer causation from correlation. - Explain missing data and
limitations.

### 📅 Week 8 — Visualization and reporting

**Topics and concepts** - Histograms, boxplots, scatterplots, line
charts - Choosing suitable plots - Titles, labels, scales, and
annotation - Data storytelling and concise reporting

**Exercises** - Create five to seven meaningful plots. - Write five
findings supported by the data. - Draft a short report for a
nontechnical reader.

**Answer checks** - Every plot should answer a question. - Use correct
units and clear labels. - Mention limitations and avoid unsupported
recommendations.

**Project 1 --- Exploratory Data Analysis**

Use [NYC Open Data](https://opendata.cityofnewyork.us/) or a manageable
public dataset.

Include: - Dataset source and data dictionary - Cleaning and quality
checks - Eight to ten analytical questions - Five to seven useful
plots - Five evidence-based findings - Limitations and a reproducible
README

**Month 2 milestone:** write SQL joins and grouped queries independently
and produce a reproducible EDA report.

---
## 🟦 Month 3 — Probability, Descriptive Statistics, and Distributions

**Goal:** Build the statistical foundation for machine learning.

### 📅 Week 9 — Descriptive statistics

**Topics and concepts** - Population versus sample - Mean, median, mode,
quantiles - Variance and standard deviation - Robust summaries and
outliers

**Exercises** - Calculate statistics manually for small lists. - Verify
calculations with NumPy. - Compare mean and median before and after
adding an extreme value.

**Answer checks** - Sample variance uses `n - 1`; population variance
uses `n`. - Explain how outliers affect different summary measures.

### 📅 Week 10 — Probability rules

**Topics and concepts** - Sample spaces and events - Addition and
multiplication rules - Conditional probability - Independence - Bayes'
theorem and counting

**Exercises** - Solve everyday probability problems. - Calculate
conditional probabilities. - Work through one Bayes' theorem example.

**Answer checks** - Do not confuse mutually exclusive events with
independent events. - Verify that probabilities are between zero and
one. - State the assumptions used.

### 📅 Week 11 — Random variables and distributions

**Topics and concepts** - Discrete and continuous random variables -
Expectation and variance - Bernoulli, binomial, normal, and Poisson
distributions - Distribution parameters and assumptions

**Exercises** - Calculate basic probabilities. - Simulate
distributions. - Compare simulated averages with theoretical
expectations.

**Answer checks** - Explain when each distribution may be appropriate. -
Simulation approximates theoretical values but will not match them
exactly every time.

### 📅 Week 12 — Sampling and the Central Limit Theorem

**Topics and concepts** - Sampling distributions - Standard error -
Central Limit Theorem - Law of large numbers - Sample size and
uncertainty

**Exercises** - Draw repeated samples and plot their means. - Compare
the spread of individual observations with sample means. - Investigate
how sample size affects standard error.

**Answer checks** - For independent observations with finite variance,
the estimated standard error of the mean is `s / sqrt(n)`. - Explain why
the sampling distribution differs from the distribution of individual
observations.

**Resources:** [StatQuest](https://www.youtube.com/@statquest), [Khan
Academy Statistics and
Probability](https://www.khanacademy.org/math/statistics-probability).

**Month 3 milestone:** explain core probability rules and distributions,
and solve applied exercises without relying entirely on library calls.

---
## 🟦 Month 4 — Statistical Inference and Experimentation

**Goal:** Reason about evidence, uncertainty, and the limitations of
conclusions.

### 📅 Week 13 — Estimation and confidence intervals

**Topics and concepts** - Point estimates - Confidence intervals -
Bootstrap resampling - Sampling variability

**Exercises** - Estimate a mean and median with bootstrap intervals. -
Compare intervals across different sample sizes.

**Answer checks** - In frequentist inference, a confidence interval is
produced by a procedure with a long-run coverage property; it is not
ordinarily interpreted as a probability assigned to a fixed parameter
after the interval is observed.

### 📅 Week 14 — Hypothesis testing

**Topics and concepts** - Null and alternative hypotheses - Test
statistics and p-values - Significance levels - Type I and Type II
errors - Statistical power

**Exercises** - State hypotheses for several questions. - Perform a
suitable test. - Explain what the p-value does and does not indicate.

**Answer checks** - A small p-value does not measure effect size. - A
p-value does not prove a hypothesis. - Statistical significance does not
automatically imply practical importance.

### 📅 Week 15 — Common statistical tests

**Topics and concepts** - t-tests - Chi-square tests - Nonparametric
alternatives - Multiple comparisons - Effect sizes and uncertainty

**Exercises** - Compare two groups. - Investigate an association between
categorical variables. - Report an effect size alongside a test result.

**Answer checks** - State assumptions and whether the method is
suitable. - Explain the result in context rather than reporting only a
p-value.

### 📅 Week 16 — Correlation, regression, and experiments

**Topics and concepts** - Correlation and confounding - Simple linear
regression - Residuals and assumptions - A/B testing - Experimental
design and causal reasoning basics

**Exercises** - Investigate an association in a dataset. - Identify a
possible confounder. - Design an A/B test with a defined outcome.

**Answer checks** - Observational association alone is insufficient to
establish causation. - Discuss bias, sample size, effect size, and
uncertainty.

**Project 2 --- Statistical Investigation**

Include: 1. A clear research question and hypotheses 2. Dataset source
and cleaning decisions 3. Exploratory analysis 4. Appropriate
statistical method and assumptions 5. Effect estimate and uncertainty 6.
A cautious conclusion and limitations

**Resource:** [OpenIntro Data](https://www.openintro.org/data/).

**Month 4 milestone:** choose a reasonable statistical method and
explain uncertainty without overstating the evidence.

---
## 🟦 Month 5 — ML Workflow, Regression, and Preprocessing

**Goal:** Understand the machine-learning workflow before learning many
algorithms.

### 📅 Week 17 — ML fundamentals

**Topics and concepts** - Supervised and unsupervised learning -
Features, targets, and prediction tasks - Baselines - Training,
validation, and test sets - Generalization, overfitting, and
underfitting

**Exercises** - Define a prediction problem. - Identify the target and
candidate features. - Build a simple baseline.

**Answer checks** - Hold back the test set until final evaluation. -
Check that features would be available at prediction time.

### 📅 Week 18 — Linear regression and regularization

**Topics and concepts** - Linear regression - Loss functions and
coefficients - Residuals and assumptions - Ridge and Lasso intuition -
Regularization

**Exercises** - Fit linear and regularized models. - Compare them with a
baseline. - Interpret coefficients with attention to units and feature
scaling.

**Answer checks** - Explain what a coefficient means under the model. -
Avoid treating association as causation.

### 📅 Week 19 — Regression evaluation

**Topics and concepts** - MAE, MSE, RMSE, and R-squared -
Cross-validation - Residual analysis - Baseline comparison

**Exercises** - Evaluate a regression model using suitable metrics. -
Compare errors across important subgroups. - Investigate large
residuals.

**Answer checks** - MAE and RMSE use the target's units; MSE uses
squared units. - R-squared is not a direct measure of whether
predictions are practically acceptable. - Explain why a baseline is
needed.

### 📅 Week 20 — Preprocessing and pipelines

**Topics and concepts** - Imputation - Numerical scaling - Categorical
encoding - `Pipeline` and `ColumnTransformer` - Data leakage prevention

**Exercises** - Build a complete preprocessing pipeline. - Handle
numerical and categorical features. - Test predictions on unseen rows.

**Answer checks** - Fit transformations only on training data or within
each training fold. - Keep preprocessing consistent between training and
inference.

**Project 3 --- Regression**

Use a suitable public housing or other tabular regression dataset.
Include: - Problem definition and baseline - Preprocessing pipeline -
Cross-validation - MAE or RMSE - Residual analysis - Final test-set
evaluation - Limitations and reproducible setup instructions

**Resource:** [Scikit-learn Getting
Started](https://scikit-learn.org/stable/getting_started.html).

---
## 🟦 Month 6 — Classification, Trees, Ensembles, and Model Selection

**Goal:** Build a strong classification workflow and compare models
fairly.

### 📅 Week 21 — Logistic regression

**Topics and concepts** - Classification versus regression - Sigmoid
function - Probability estimates - Decision thresholds - Logistic
regression

**Exercises** - Train a classifier. - Change the decision threshold. -
Compare precision and recall.

**Answer checks** - A threshold changes predicted labels even when model
scores stay the same. - Explain why the threshold should reflect the
task's costs.

### 📅 Week 22 — Classification metrics

**Topics and concepts** - Confusion matrix - Precision, recall,
specificity, F1 - ROC-AUC and PR-AUC - Class imbalance

**Exercises** - Evaluate a model on an imbalanced dataset. - Compare
accuracy with precision and recall. - Justify a primary metric.

**Answer checks** - Accuracy alone can be misleading when classes are
imbalanced. - Select metrics according to the cost of false positives
and false negatives.

### 📅 Week 23 — Trees and ensembles

**Topics and concepts** - Decision trees - Random forests - Gradient
boosting - XGBoost/CatBoost awareness - Feature importance limitations

**Exercises** - Compare a tree, random forest, and boosting model. -
Keep splits and evaluation procedures consistent. - Inspect overfitting
and model complexity.

**Answer checks** - Compare models using the same data and metric. -
Avoid choosing a model solely because its training score is high.

### 📅 Week 24 — Validation and tuning

**Topics and concepts** - Cross-validation - Hyperparameter search -
Stratified splitting - Class weights - Calibration - Error analysis and
leakage

**Exercises** - Tune a model using validation data or
cross-validation. - Analyze false positives and false negatives. -
Compare performance across relevant groups.

**Answer checks** - Do not tune repeatedly against the test set. - Keep
related or duplicate records from leaking across splits where
relevant. - Document model selection decisions.

**Project 4 --- Classification**

Possible dataset: [UCI Breast Cancer Wisconsin
Diagnostic](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)
or a suitable public churn dataset.

Include: - Majority-class or simple baseline - At least three model
comparisons - Appropriate metrics - Cross-validation and tuning - Error
analysis - Feature-importance caveats - Reproducible final evaluation

For health-related datasets, present the project as educational
modeling, not medical advice.

---
## 🟦 Month 7 — Advanced SQL, Feature Engineering, Clustering, and PCA

**Goal:** Handle realistic data workflows and learn beyond supervised
prediction.

### 📅 Week 25 — Advanced SQL

**Topics and concepts** - Common table expressions - Window functions -
`ROW_NUMBER`, `RANK`, `LAG` - Running totals and rolling aggregates -
Basic query-plan awareness

**Exercises** - Solve analytical SQL problems. - Calculate rankings and
running totals. - Compare window-function output with grouped
aggregates.

**Answer checks** - Verify results using small hand-checkable tables. -
Understand when a window function preserves rows instead of collapsing
them.

### 📅 Week 26 — Feature engineering

**Topics and concepts** - Date/time features - Categorical cardinality -
Domain-driven features - Missingness indicators - Leakage prevention

**Exercises** - Create useful features for an existing ML project. -
Compare model results before and after feature engineering.

**Answer checks** - Every feature must be available at prediction
time. - Evaluate improvements with the same validation process.

### 📅 Week 27 — Clustering

**Topics and concepts** - K-means - Distance metrics - Scaling -
Choosing cluster counts - Silhouette score and stability

**Exercises** - Cluster a dataset with scaled features. - Compare a few
plausible cluster counts. - Profile the resulting groups.

**Answer checks** - Clusters are not automatically meaningful business
segments. - Explain the effect of scaling and the limitations of
internal metrics.

### 📅 Week 28 — PCA and anomaly detection

**Topics and concepts** - Dimensionality reduction - Principal
components - Explained variance - Anomaly-detection introduction

**Exercises** - Scale data and apply PCA. - Plot components and inspect
explained variance. - Explain information lost when reducing dimensions.

**Answer checks** - PCA components are combinations of features, not
automatically meaningful labels. - Fit scaling and PCA using training
data when part of a predictive workflow.

**Mini-project:** perform a segmentation or unsupervised-learning study
with documented preprocessing, evaluation, interpretation, and
limitations.

**Resources:** [Scikit-learn
Clustering](https://scikit-learn.org/stable/modules/clustering.html) and
[PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca).

---
## 🟦 Month 8 — Explainability, Dashboards, and Data Storytelling

**Goal:** Turn technical analysis into a useful decision-support tool.

### 📅 Week 29 — Explainability

**Topics and concepts** - Permutation importance - Tree-based
importance - SHAP concepts - Correlated features - Local versus global
explanations

**Exercises** - Explain selected predictions. - Compare importance
methods. - Record where an explanation may be misleading.

**Answer checks** - Feature importance is not proof of causality. -
Correlated features can make importance difficult to interpret.

### 📅 Week 30 — Dashboard design

**Topics and concepts** - KPIs and user questions - Filters and chart
selection - Layout and visual hierarchy - Accessibility and clear labels

**Exercises** - Sketch a dashboard before coding. - Choose a few
meaningful metrics. - Ask whether each visual answers a specific
question.

### 📅 Week 31 — Streamlit

**Topics and concepts** - App structure - User inputs and filters -
Tables and charts - Input validation - Handling empty results

**Exercises** - Build an interactive dashboard or prediction
interface. - Test valid and invalid input combinations.

### 📅 Week 32 — Reporting and recommendations

**Topics and concepts** - Executive summaries - Evidence-based
recommendations - Limitations and caveats - Reproducibility and
technical writing

**Exercises** - Write a one-page report. - Include findings, evidence,
recommendations, limitations, and next steps. - Ask a reader to identify
the main conclusion quickly.

**Project 5 --- Interactive Data App**

Deliver: - Interactive dashboard - Documented dataset source - Useful
filters and visualizations - Clear explanation of findings - Limitations
and setup instructions

**Resources:** [Streamlit](https://docs.streamlit.io/) and
[Matplotlib](https://matplotlib.org/stable/tutorials/).

---
## 🟦 Month 9 — Software Engineering for ML

**Goal:** Move from notebook-only work to testable, reusable code.

### 📅 Week 33 — Project structure and environments

**Topics and concepts** - Modules and packages - Configuration - Virtual
environments and dependencies - Logging - Reproducibility

**Exercises** - Refactor notebook logic into reusable functions. - Add a
clear project structure. - Document setup and execution.

**Answer checks** - The project should run from documented commands in a
clean environment. - Avoid relying on hidden notebook state or absolute
local paths.

### 📅 Week 34 — Testing and data validation

**Topics and concepts** - Unit tests with pytest - Edge cases - Data
validation - Deterministic behavior - Testable function design

**Exercises** - Test cleaning functions and feature transformations. -
Include missing values, empty inputs, invalid types, and boundary cases.

**Answer checks** - Tests should fail when behavior is deliberately
broken. - Cover expected and invalid inputs.

### 📅 Week 35 — REST APIs and FastAPI

**Topics and concepts** - HTTP methods and status codes - JSON - Request
and response schemas - Input validation - API documentation

**Exercises** - Create a prediction endpoint. - Validate request
features. - Return predictions and useful error responses.

**Answer checks** - Invalid requests should not silently produce
unreliable predictions. - Document an example request and response.

### 📅 Week 36 — Serialization and Docker

**Topics and concepts** - Saving and loading models - Model and
preprocessing consistency - Docker images and containers - Environment
variables - Application configuration

**Exercises** - Package the prediction API. - Build and run the
container. - Verify inference works outside the training notebook.

**Answer checks** - Use the same fitted preprocessing pipeline during
inference. - Document reproducible commands and avoid committing
secrets.

**Mini-project:** serve the Month 6 classifier through an API, with
preprocessing, tests, documentation, and a container.

**Resources:** [pytest](https://docs.pytest.org/),
[FastAPI](https://fastapi.tiangolo.com/tutorial/), [Docker Get
Started](https://docs.docker.com/get-started/).

---
## 🟦 Month 10 — Experiment Tracking, CI, Deployment, and Monitoring

**Goal:** Build a small but credible production-style ML workflow.

### 📅 Week 37 — MLflow tracking

**Topics and concepts** - Experiment names and runs - Parameters,
metrics, artifacts - Model comparison - Reproducibility

**Exercises** - Log multiple experiments. - Compare model configurations
and results.

**Answer checks** - Each run should connect its configuration, metrics,
and artifacts.

### 📅 Week 38 — Model documentation and versioning

**Topics and concepts** - Model versioning concepts - Artifact
management - Reproducible data and code - Model cards and limitations

**Exercises** - Document intended use, data source, evaluation, and
limitations. - Identify the exact model artifact used by the API.

### 📅 Week 39 — Continuous integration

**Topics and concepts** - GitHub Actions - Automated tests - Linting and
formatting - Build checks

**Exercises** - Add a workflow that runs tests on changes. -
Deliberately introduce a failing test and verify that CI detects it.

### 📅 Week 40 — Deployment and monitoring concepts

**Topics and concepts** - Deployment options - Secrets and
configuration - Data drift versus performance drift - Logging and
monitoring signals - Retraining triggers

**Exercises** - Run or deploy a small service reproducibly. - Write a
monitoring plan identifying what should be measured and why.

**Answer checks** - Distinguish a change in input data from a decline in
model performance. - Explain that monitoring requires appropriate data
and, for performance monitoring, often reliable outcome labels.

**Milestone:** a tested model service with logged experiments,
documented artifacts, reproducible setup, and a realistic monitoring
plan.

**Resources:** [MLflow
Quickstart](https://mlflow.org/docs/latest/ml/getting-started/quickstart/)
and [GitHub Actions](https://docs.github.com/en/actions).

---
## 🟦 Month 11 — Capstone Project

**Goal:** Combine analysis, statistics, ML, and software engineering
into one polished project.

### 📅 Week 41 — Problem framing and proposal

**Topics and concepts** - Problem definition - Research question -
Dataset selection - Data dictionary - Evaluation plan

**Exercises** - Write a one-page proposal. - Define the target, intended
use, success metric, and potential limitations.

**Answer checks** - The target must be measurable. - The data must be
suitable and legally/ethically usable. - The evaluation method must
match the question.

### 📅 Week 42 — Data preparation and EDA

**Topics and concepts** - Data ingestion and cleaning - Exploratory
analysis - Statistical investigation - Feature pipeline

**Exercises** - Create a reproducible analysis and training dataset. -
Document missingness, duplicates, and data-quality decisions.

**Answer checks** - Check for target leakage and train/test
contamination. - Verify all transformations can be reproduced.

### 📅 Week 43 — Modeling and evaluation

**Topics and concepts** - Baselines - Model comparison and tuning -
Error analysis - Explainability - Limitations

**Exercises** - Compare several reasonable models. - Select a final
model using a documented procedure. - Record experiments that did not
improve results.

**Answer checks** - Compare models fairly. - Avoid choosing a model only
because it has the highest training score.

### 📅 Week 44 — Application integration

**Topics and concepts** - API or dashboard integration - Testing -
Documentation - Demo preparation

**Exercises** - Connect the model to a usable interface. - Test the
end-to-end workflow. - Write reproduction instructions.

**Answer checks** - Another person should be able to follow the README
and reproduce the key result.

### 🎯 Choose one specialization

-   **Applied Data Science:** experimentation, advanced SQL,
    forecasting, causal reasoning basics.
-   **ML Engineering:** APIs, reliability, deployment, tests, experiment
    tracking, monitoring.
-   **Research-oriented ML:** paper reading, baseline reproduction,
    experimental methods.
-   **Deep learning introduction:** neural-network fundamentals and
    PyTorch, provided classical ML foundations are solid.

---
## 🟦 Month 12 — Portfolio, Revision, and Master's Preparation

### 📅 Week 45 — Portfolio audit

-   Polish READMEs and project structure.
-   Remove broken instructions and unexplained code.
-   Reproduce results from a fresh environment.

**Check:** a reviewer can understand each project's question, method,
results, and limitations.

### 📅 Week 46 — Statistics and ML revision

-   Revise probability, inference, regression, classification, metrics,
    and leakage.
-   Complete a timed self-test without notes.
-   Correct errors in the revision notebook.

**Check:** explain concepts and solve problems without copying a worked
example.

### 📅 Week 47 — SQL, Python, and technical communication

-   Solve mixed SQL questions.
-   Practice explaining a project aloud.
-   Review data structures and Python skills relevant to your work.

**Check:** explain the problem, data, method, evaluation, limitations,
and practical value clearly.

### 📅 Week 48 — Graduate program research

-   Shortlist Data Science, Statistics, AI, or Computer Science
    programs.
-   Record prerequisites, curriculum, thesis options, costs, funding,
    deadlines, and required documents.
-   Verify requirements on official university websites.

**Check:** maintain a comparison sheet and realistic application
timeline.

### 📅 Week 49 — Capstone polish

-   Fix high-impact defects.
-   Repeat tests and deployment checks.
-   Verify data and model documentation.

**Check:** reproduce the capstone from documented instructions.

### 📅 Week 50 — Academic communication

-   Prepare an academic CV draft.
-   Outline a statement of purpose based on genuine interests and
    experiences.
-   Identify suitable faculty for recommendation requests well in
    advance.

**Check:** all claims are accurate and supported by actual coursework,
projects, or experience.

### 📅 Week 51 — Portfolio review and demo

-   Request feedback on your repository or demonstration.
-   Practice answering questions about methodology and limitations.
-   Improve unclear explanations.

**Check:** demonstrate the project without relying on undocumented
steps.

### 📅 Week 52 — Annual assessment

-   Review the milestone checklist.
-   Identify the three biggest remaining skill gaps.
-   Choose the next 3--6 months of specialization.
-   Update your graduate application timeline.

**Check:** make the next learning plan based on demonstrated strengths
and weaknesses, not simply on the number of courses completed.

---
# 📝 4. Notes and Revision System

Keep notes separate from projects. A local folder or a GitHub repository
works well.

## 🧱 Suggested structure

``` text
data-science-learning/
├── notes/
│   ├── 01-python-numpy-pandas.md
│   ├── 02-sql.md
│   ├── 03-probability.md
│   ├── 04-statistics-inference.md
│   ├── 05-machine-learning.md
│   ├── 06-model-evaluation.md
│   └── 07-ml-engineering.md
├── exercises/
│   ├── sql/
│   ├── statistics/
│   └── machine-learning/
├── projects/
│   ├── eda/
│   ├── predictive-model/
│   ├── dashboard/
│   └── capstone/
└── revision/
    ├── mistakes.md
    ├── formula-sheet.md
    └── monthly-reviews.md
```

## 🧾 Topic note template

For each important concept, record:

1.  **Definition and purpose:** What is it, and why is it useful?
2.  **Intuition:** Explain it in your own words with a small example.
3.  **Formula or algorithm:** Define the symbols and work through an
    example.
4.  **Code example:** Include a minimal example and explain its output.
5.  **Assumptions and mistakes:** Explain when it applies and where it
    can fail.
6.  **Recall questions:** Write three to five questions to answer
    without notes.

## 🔍 Example: precision and recall

-   **Precision:** among predicted positives, how many were actually
    positive?
-   **Recall:** among actual positives, how many were identified?
-   **Precision:** `TP / (TP + FP)`
-   **Recall:** `TP / (TP + FN)`
-   **Precision matters more when:** false positives are especially
    costly.
-   **Recall matters more when:** missing positive cases is especially
    costly.
-   **Common mistake:** relying on accuracy alone for an imbalanced
    dataset.
-   **Recall question:** if a model identifies half the actual positive
    cases, what is its recall? **Answer: 50%.**

## ⏱️ Spaced revision schedule

| When | Activity |
|---|---|
| Same day | Summarize the main idea from memory |
| Two days later | Answer recall questions and redo one exercise |
| One week later | Solve a new problem without following a tutorial |
| One month later | Complete a mixed-topic assessment |
| End of phase | Explain the topic and demonstrate it in code without notes |

Keep a `mistakes.md` file with: mistake, why it happened, correct
reasoning, and a new test to prevent it.

---
# ✅ 5. Exercise Levels and Answer Checks

For every major topic, complete three levels:

1.  **Understand:** reproduce a small example, calculate an answer
    manually, or explain the concept.
2.  **Apply:** solve a new problem using a dataset and different
    requirements from the tutorial.
3.  **Combine:** apply the concept alongside previous topics in a
    mini-project.

## 🧪 Example answer-check standards

### SQL: top three categories by sales

Expected logic: group by category, sum sales, sort totals descending,
return three categories. If joins are involved, verify they do not
multiply sales rows.

### Statistics: compare two group averages

Expected output: group summaries, an appropriate effect estimate,
uncertainty, assumptions, and a cautious conclusion. A p-value alone is
not a complete analysis.

### Regression: evaluate a price prediction model

Expected output: baseline, cross-validation, MAE or RMSE in the target's
units, residual analysis, final test result, and an explanation of
whether the error is practically acceptable.

### Classification: detect a rare event

Expected output: majority-class baseline, confusion matrix, precision,
recall, and a suitable PR-AUC or other task-relevant metric. Justify the
threshold.

### ML engineering: serve a saved model

Expected output: validated inputs, consistent preprocessing, useful
error responses, tests, reproducible setup, and an example
request/response.

For open-ended ML work, there may not be one correct score. Sound
methodology, validation, interpretation, and reproducibility matter as
much as the metric.

---
# 🧱 6. Portfolio Projects

## 🧩 Project 1 — Exploratory Data Analysis (Month 2)

**Skills:** Pandas, SQL, statistics, visualization, communication.

**Tasks** - Select and document a public dataset. - Clean missing,
duplicate, and inconsistent records. - Answer eight to ten analytical
questions. - Produce a report with five findings and limitations.

**Acceptance criteria:** reproducible notebook, data dictionary,
meaningful plots, README, and conclusions supported by results.

## 🧩 Project 2 — Predictive Modeling (Month 6)

**Skills:** scikit-learn, feature engineering, model evaluation,
validation.

**Tasks** - Define a regression or classification problem. - Establish a
baseline and compare at least three models. - Use cross-validation and
appropriate metrics. - Analyze errors, feature importance, and
limitations.

**Acceptance criteria:** leakage-free pipeline, justified model choice,
recorded experiments, and reproducible evaluation.

## 🧩 Project 3 — Interactive Data App (Month 8)

**Skills:** Streamlit, visualization, reporting, basic application
design.

**Tasks** - Build an interactive dashboard or prediction interface. -
Add filters and validated inputs. - Explain the results and
limitations. - Provide setup instructions.

**Acceptance criteria:** usable interface, correct calculations,
sensible handling of empty results, and clear documentation.

## 🧩 Project 4 — Production-Style ML Capstone (Months 9--12)

**Skills:** Python, scikit-learn, FastAPI, pytest, Docker, MLflow,
GitHub Actions.

**Tasks** - Package the model and preprocessing. - Serve predictions
through an API. - Add automated tests and experiment tracking. -
Document model limitations, versioning, and monitoring ideas.

**Acceptance criteria:** another person can reproduce the model, run
tests, start the service, and make a prediction using the README.

A modest project with sound methodology is better than an
impressive-looking project with leakage or unsupported claims.

---
# 📚 7. Free Learning Resource Library

Use one primary resource per subject. Avoid collecting courses before
completing exercises.

| Subject | Resource |
|---|---|
| Practical data analysis and introductory ML | [Kaggle Learn](https://www.kaggle.com/learn) |
| Statistics and ML intuition | [StatQuest](https://www.youtube.com/@statquest) |
| Interactive SQL practice | [SQLBolt](https://sqlbolt.com/) |
| NumPy | [NumPy documentation](https://numpy.org/doc/stable/) |
| Pandas | [Pandas documentation](https://pandas.pydata.org/docs/) |
| Statistics and scientific computing | [SciPy](https://docs.scipy.org/doc/scipy/) and [Statsmodels](https://www.statsmodels.org/stable/) |
| Classical ML | [Scikit-learn](https://scikit-learn.org/stable/getting_started.html) |
| Visualization | [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/) and [Seaborn tutorials](https://seaborn.pydata.org/tutorial.html) |
| Interactive dashboards | [Streamlit](https://docs.streamlit.io/) |
| Testing | [pytest](https://docs.pytest.org/) |
| APIs | [FastAPI](https://fastapi.tiangolo.com/tutorial/) |
| Containers | [Docker Get Started](https://docs.docker.com/get-started/) |
| Experiment tracking | [MLflow](https://mlflow.org/docs/latest/ml/getting-started/quickstart/) |
| CI | [GitHub Actions](https://docs.github.com/en/actions) |
| Later deep learning | [PyTorch beginner tutorials](https://docs.pytorch.org/tutorials/beginner/basics/) |

Prioritize NumPy, Pandas, SQL, statistics, scikit-learn, and
visualization in the first eight months. Begin PyTorch only when the
classical ML workflow and evaluation concepts are solid.

---
# 🎯 8. Monthly Milestone Checklist

Mark each milestone complete only when you can demonstrate it
independently.

-   [ ] **Month 1:** Manipulate arrays and tables; clean a dataset and
    explain data-quality decisions.
-   [ ] **Month 2:** Write joins and aggregations; produce a
    reproducible EDA report.
-   [ ] **Month 3:** Explain probability, distributions, sampling, and
    standard error; solve applied exercises.
-   [ ] **Month 4:** Choose suitable statistical methods and explain
    uncertainty and limitations.
-   [ ] **Month 5:** Train a regression model with a baseline, pipeline,
    and correct validation.
-   [ ] **Month 6:** Compare classification models with justified
    metrics and error analysis.
-   [ ] **Month 7:** Use window-function SQL, feature engineering, and
    basic clustering/PCA.
-   [ ] **Month 8:** Deliver an interactive dashboard and evidence-based
    report.
-   [ ] **Month 9:** Refactor code into modules and tests; expose
    predictions through an API.
-   [ ] **Month 10:** Track experiments, package the application, and
    run automated checks.
-   [ ] **Month 11:** Complete a capstone proposal, implementation, and
    evaluation.
-   [ ] **Month 12:** Publish a polished portfolio and prepare a
    realistic graduate-study plan.

---
# 🎓 9. Master's Abroad Preparation

Treat graduate-school preparation as a parallel activity.

-   **Months 1--4:** Maintain strong university grades, revise
    probability, statistics, and linear algebra, and keep records of
    relevant coursework.
-   **Months 5--8:** Explore Data Science, Statistics, AI, and Computer
    Science programs. Compare prerequisites, curriculum, thesis options,
    and funding.
-   **Months 9--10:** Identify research topics you genuinely want to
    explore. Read introductory papers and document questions arising
    from your projects.
-   **Months 11--12:** Prepare an academic CV, shortlist programs,
    outline a statement of purpose, and plan recommendation requests
    early.

Verify deadlines, English-language requirements, test policies, funding
eligibility, and document requirements on official university pages.
Requirements vary by university and intake. A portfolio demonstrates
technical ability but does not replace grades, prerequisites, or
research preparation.

---
# 📜 10. Rules for the Year

1.  Do not rush through a topic if you cannot explain it or solve a
    basic problem independently.
2.  Do not copy complete project notebooks. Learn from references, then
    write your own analysis and explain your decisions.
3.  Keep projects reproducible. Track data sources, dependencies,
    preprocessing, evaluation, and setup instructions.
4.  Review fundamentals before adding tools. Strong SQL, statistical
    reasoning, validation, and clear Python code matter more than a long
    list of frameworks.
5.  Do not confuse a project score with real-world usefulness. Evaluate
    data quality, generalization, error costs, limitations, and whether
    the result answers the original question.
6.  Use a weekly buffer for university exams and assignments. Resume
    from the last unfinished task rather than restarting the plan.

## 🚀 First Action

Start Week 1 with NumPy broadcasting and array operations. Create your
notes folder, complete a short exercise set, and commit your work to
Git. Move to Week 2 when you can explain your results without relying on
example code.

The intended outcome after twelve months is a strong foundation in
applied Data Science, the ability to build and evaluate classical ML
models properly, experience packaging a model as a tested application,
and a credible portfolio for internships, early-career opportunities,
and future master's applications. This is a structured target, not a
guarantee of employment or admission.

---
*Learn the concepts. Test the assumptions. Build the solution.*
