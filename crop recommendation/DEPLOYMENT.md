# Crop Recommendation Deployment Guide

This guide explains how to deploy the Crop Recommendation application to production.

## Architecture

The application consists of:
- **Frontend**: Static HTML/CSS/JS served by Node.js Express
- **Backend API Gateway**: Node.js Express server handling authentication, users, and proxying to Python API
- **ML Backend**: Python FastAPI server for crop recommendations using Random Forest and SHAP
- **Database**: MongoDB for user data and predictions

## Local Deployment with Docker

### Prerequisites
- Docker and Docker Compose installed

### Steps

1. **Clone/Build the images**:
   ```bash
   docker-compose build
   ```

2. **Start the services**:
   ```bash
   docker-compose up -d
   ```

3. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API Docs: http://localhost:8001/docs
   - MongoDB: localhost:27017

4. **Stop the services**:
   ```bash
   docker-compose down
   ```

## Production Deployment

### Option 1: Docker Compose on VPS

1. Set up a VPS (e.g., DigitalOcean, AWS EC2)
2. Install Docker and Docker Compose
3. Clone your repository
4. Update `.env` with production values:
   ```
   MONGO_URI=mongodb://mongodb:27017/crop_recommendation_db
   PYTHON_API_URL=http://backend:8001
   JWT_SECRET=your-secure-secret
   GEMINI_API_KEY=your-gemini-key
   ```
5. Run `docker-compose up -d`

### Option 2: Cloud Platforms

#### AWS ECS
1. Build and push images to Amazon ECR
2. Create ECS cluster with Fargate
3. Use docker-compose.yml as task definition
4. Set up ALB for load balancing

#### Google Cloud Run
1. Build images and push to Google Container Registry
2. Deploy each service as Cloud Run service
3. Use Cloud Load Balancing

#### Railway
1. Connect GitHub repository
2. Railway auto-detects docker-compose.yml
3. Set environment variables in dashboard

### Environment Variables

Create a `.env` file with:
```
MONGO_URI=mongodb://your-mongodb-uri
PYTHON_API_URL=http://your-backend-url:8001
JWT_SECRET=your-jwt-secret
GEMINI_API_KEY=your-gemini-api-key
AGMARKET_API_URL=your-agmarket-url
AGMARKET_API_KEY=your-agmarket-key
```

For MongoDB Atlas (cloud):
```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/crop_recommendation_db
```

## Security Considerations

- Use strong JWT secrets
- Enable HTTPS in production
- Configure CORS properly
- Use environment variables for all secrets
- Regularly update dependencies

## Monitoring

- Monitor logs with `docker-compose logs`
- Set up health checks for all services
- Use MongoDB Atlas monitoring for database