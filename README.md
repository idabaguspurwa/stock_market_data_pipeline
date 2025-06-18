# Stock Market Data Pipeline

**Author:** Ida Bagus Gede Purwa Manik Adiputra

## Overview

This project implements a comprehensive stock market data pipeline using Apache Airflow, Apache Spark, MinIO, and Docker. The pipeline extracts NVDA stock price data from Yahoo Finance API, processes and transforms the data using Spark, stores it in MinIO object storage, and loads it into a data warehouse for analysis.

## Architecture

The pipeline consists of the following components:

- **Apache Airflow**: Orchestrates the entire data pipeline workflow
- **Apache Spark**: Processes and transforms raw stock data
- **MinIO**: Object storage for raw and processed data
- **Docker**: Containerization for all services
- **Data Warehouse**: Final destination for processed stock data

## Project Structure

```
├── dags/                           # Airflow DAGs
│   ├── stock_market.py            # Main stock market pipeline DAG
│   └── random_number.py           # Example DAG
├── include/
│   ├── stock_market/
│   │   └── tasks.py               # Stock market task functions
│   ├── helpers/
│   │   └── minio.py               # MinIO helper functions
│   └── data/                      # Data storage directory
├── spark/
│   ├── master/                    # Spark master configuration
│   ├── worker/                    # Spark worker configuration
│   └── notebooks/
│       └── stock_transform/       # Spark transformation jobs
├── docker-compose.override.yml    # Docker compose overrides
├── Dockerfile                     # Main Dockerfile
├── requirements.txt               # Python dependencies
└── tests/                         # Test files
```

## Features

### Data Pipeline Workflow

1. **API Availability Check**: Validates stock API connectivity
2. **Data Extraction**: Fetches stock price data from external APIs
3. **Data Storage**: Stores raw JSON data in MinIO
4. **Data Transformation**: Processes data using Spark to format prices
5. **Data Loading**: Loads processed data into the data warehouse

### Supported Operations

- Real-time stock price extraction
- Historical data processing
- Data format transformation (JSON to CSV)
- Automated daily pipeline execution
- Error handling and retry mechanisms

## Installation & Setup

### Prerequisites

- Docker Desktop (minimum 8GB RAM allocation)
- Astronomer CLI
- Python 3.8+

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd stock-market-pipeline
   ```

2. **Start the services**
   ```bash
   astro dev start
   ```

3. **Access the services**
   - Airflow UI: http://localhost:8080
   - Spark Master UI: http://localhost:8081
   - MinIO Console: http://localhost:9000

### Configuration

#### Airflow Connections

Set up the following connections in Airflow:

1. **MinIO Connection** (`minio`)
   - Connection Type: S3
   - Host: http://host.docker.internal:9000
   - Login: minio
   - Password: minio123

2. **Stock API Connection** (`stock_api`)
   - Connection Type: HTTP
   - Host: <your-stock-api-endpoint>
   - Extra: {"headers": {"your-api-headers"}}

#### Environment Variables

```bash
# Spark Configuration
AWS_ACCESS_KEY_ID=minio
AWS_SECRET_ACCESS_KEY=minio123
ENDPOINT=http://host.docker.internal:9000

# Stock Market Configuration
BUCKET_NAME=stock-market
```

## Usage

### Running the Pipeline

1. **Manual Trigger**: Navigate to Airflow UI and trigger the `stock_market` DAG
2. **Scheduled Execution**: Pipeline runs daily at midnight (configurable)

### Monitoring

- **Airflow UI**: Monitor DAG runs, task status, and logs
- **Spark UI**: Track Spark job execution and performance
- **MinIO Console**: View stored data objects and bucket contents

### Data Access

Processed stock data is available in:
- **MinIO**: `stock-market/{SYMBOL}/formatted_prices/`
- **Data Warehouse**: Via configured connection

## Troubleshooting

### Common Issues

1. **Spark Job Stuck**: 
   ```bash
   astro dev kill && astro dev start
   ```

2. **Memory Issues**: Ensure Docker Desktop has at least 8GB RAM allocated

3. **Connection Errors**: Verify MinIO and API connections in Airflow

### Debugging

- Check Airflow task logs for detailed error messages
- Monitor Spark application logs in the Spark UI
- Verify data integrity in MinIO console

## Development

### Adding New Stock Symbols

1. Update the DAG configuration in `dags/stock_market.py`
2. Modify the API endpoint in `include/stock_market/tasks.py`

### Extending Transformations

1. Edit the Spark job in `spark/notebooks/stock_transform/stock_transform.py`
2. Add new transformation logic as needed

## Dependencies

### Python Packages
- `apache-airflow`
- `minio==7.2.14`
- `apache-airflow-providers-docker==4.0.0`
- `pyspark`

### Docker Images
- `bde2020/spark-base:3.3.0-hadoop3.3`
- `minio/minio`
- Custom Airflow image with required providers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

**Ida Bagus Gede Purwa Manik Adiputra**

For questions or support, please open an issue in the repository.
