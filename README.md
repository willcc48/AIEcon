# AI Economist Policy
Web dashboard and extension of Salesforce's AI Economist multi-agent reinforcement learning tax policy environment. Streamlit is being used as a Python web framework. Conda environment used with Python 3.7. ai_economist directory holds base code and agent models, etc.

Install AI Economist locally, allowing for custom changes in AI Economist environments and models.

      cd ai-economist
      pip install -e .
      
Also:

      pip install streamlit

Typical packages are needed like matplotlib, numpy (use conda environment). In ./app:

      streamlit run app.py
