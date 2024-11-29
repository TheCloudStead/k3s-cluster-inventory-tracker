# k3s-cluster-inventory-tracker

### Introduction

This repository contains the code for setting up an inventory tracking tool on a k3s cluster using a cron job and BeautifulSoup. The tool helps automate scraping and tracking items in an inventory. You can check out the detailed Medium article about the project here:

**[Automated Inventory Tracking with k3s CronJob and BeautifulSoup](https://thecloudstead.medium.com/k3s-cronjob-and-beautifulsoup-for-inventory-tracking-cc8b48ea7ac5)**

### Prerequisites

- A k3s cluster up and running.
- Docker installed on your local machine for building images.
- `kubectl` configured to interact with your k3s cluster.

### Getting Started

Clone the repository and move into the project directory:

```bash
git clone https://github.com/TheCloudStead/k3s-cluster-inventory-tracker
cd k3s-cluster-inventory-tracker
```

### Configuration

Before deploying, a few updates are needed to ensure the application works with your environment:

1. **Update the image URL**:

   - Open `cronjob.yaml` and update the container image URL to point to your desired Docker registry.
   - Open `build.sh` and update the image URL to your Docker registry.

2. **Modify environment variables and logic**:

   - Edit `app.py` to customize environment variables to suit your use case.
   - Review and modify the `check_status` logic if you need different criteria for tracking inventory.

### Build and Deploy

After making the necessary updates, run the following scripts:

1. **Build the Docker Image**:

   ```bash
   sh ./build.sh
   ```

   This will build the Docker image and push it to the specified registry.

2. **Deploy to k3s Cluster**:

   ```bash
   sh ./apply.sh
   ```

   This will apply the necessary Kubernetes resources to your k3s cluster, including the CronJob for running the inventory tracker periodically.

### Files Overview

- **cronjob.yaml**: Defines the Kubernetes CronJob that runs periodically to check inventory status.
- **build.sh**: Script to build and push the Docker image.
- **app.py**: The core Python script that performs inventory tracking using BeautifulSoup.

### Updating Inventory Logic

If you need to adjust the inventory scraping logic, make edits in `app.py`. This script uses BeautifulSoup to scrape the inventory data, and you can customize it to match the structure of the page you are tracking.

### Tips

- Ensure you have sufficient permissions to push images to your Docker registry.
- Make sure your k3s cluster has access to the image registry for pulling the latest images.
- Test your changes locally before deploying them to your cluster to avoid runtime surprises.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Acknowledgments

Thank you to the readers of my Medium articles!