FROM python:3.11-bookworm

WORKDIR /app

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false

EXPOSE 8080

CMD ["cat"]
# CMD ["uvicorn", "data_engineering_demo.__init__:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
