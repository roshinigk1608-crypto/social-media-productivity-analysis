# Analysis Preregistration

## Research question
Is there a significant relationship between daily social media usage and the productivity levels of college students?

## Hypotheses
Null Hypothesis (H0):
There is no significant relationship between daily social media usage and student productivity.

Alternative Hypothesis (H1):
There is a significant negative relationship between daily social media usage and student productivity.

Expected Direction:
Students who spend more time on social media are expected to report lower productivity levels.

## Population, sample, and exclusions

Target Population:
College students who actively use social media platforms.

Sample:
A planned sample of 50 college students will be selected through a voluntary online survey.

Unit of Analysis:
Individual college students.

Inclusion Rules:

- Currently enrolled college students.
- Active users of at least one social media platform.
- Participants who voluntarily agree to participate.
- Participants who provide complete survey responses.

Exclusion Rules:

- Incomplete survey responses.
- Duplicate responses.
- Responses with missing or invalid main variable values.

Stopping Rule:
Data collection will stop after obtaining 50 valid responses or after two weeks, whichever occurs first.

## Variables and measures
Outcome Variable:
Student productivity level, measured using a self-reported rating scale from 1 to 10.

Predictor Variable:
Daily social media usage, measured in hours per day.

Control Variables:

- Daily sleep duration.
- Daily study hours.
- Number of social media platforms used.

Data Collection:
Data will be collected through a structured online questionnaire.

Data Transformation:
Social media usage will be measured in hours per day. Productivity will be measured using a numerical rating from 1 to 10.

Missing Data Handling:
Incomplete responses containing missing values in the main variables will be excluded from the primary analysis.

## Analysis plan

Statistical Test:
Spearman's rank correlation will be used to examine the relationship between social media usage and student productivity.

Assumptions:
The observations should be independent, and the relationship should be reasonably monotonic.

Significance Level:
The alpha level will be set at 0.05.

Effect Size:
Spearman's correlation coefficient will measure the strength and direction of the relationship.

Uncertainty Intervals:
A 95% confidence interval will be calculated using bootstrap resampling where feasible.

Robustness Checks:
Results will be examined using descriptive statistics, scatter plots, and sensitivity checks for unusual observations.

Tools:
Python, Pandas, NumPy, Matplotlib, and SciPy will be used for data processing, statistical analysis, and visualization.

Interpretation:
A significant negative correlation will suggest that higher social media usage is associated with lower student productivity. The study will not claim that social media usage directly causes reduced productivity.

## Deviations
Any deviation from the original research plan will be recorded with a timestamp and a clear explanation.

Changes to the research question, sample selection, variables, or statistical methods will be documented transparently.

The original analysis plan will be maintained unless a justified change is necessary.
