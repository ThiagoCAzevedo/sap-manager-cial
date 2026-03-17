
# SAP  Manager Microservice

The SAP Manager microservice is responsible for managing and orchestrating the lifecycle of SAP sessions used by the CIAL system.

Its primary purpose is to centralize the creation, maintenance, and controlled access to a shared SAP session, ensuring consistency and reducing redundant session initialization across the platform.

By exposing RESTful endpoints, this service provides a unified interface that allows other microservices to request, validate, and interact with an active SAP session in a secure and efficient manner.
This approach promotes reusability, minimizes processing overhead, and standardizes SAP connectivity within the ecosystem.

#### Key Responsibilities
- Centralize SAP session initialization and management.
- Provide controlled access to the SAP session through dedicated endpoints.
- Ensure that dependent microservices can reliably interact with SAP without the need to create their own sessions.
- Reduce duplicate connections and optimize resource usage across the system.
- Act as an integration layer between the internal microservices architecture and the SAP backend.
## 🟢 API Reference 

### Create SAP session

```http
  POST /sap-manager/session
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| _None_ | — | This endpoint does not receive parameters |

**Description:** Creates and stores a new SAP session.


### Get SAP status

```http
  GET /sap-manager/status
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| _None_     | — | Returns information about the current SAP session |

**Description:** Retrieves the current stored SAP session status, including type and basic metadata.


### Get stored SAP session

```http
    GET /sap-manager/session
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| _None_     | — | Returns the serialized stored SAP session |

**Description:** Retrieves the SAP session stored in memory, with detailed serialized fields.



## 🟢 Run Locally

Clone the project

```bash
  git clone https://github.com/ThiagoCAzevedo/auth-cial.git
```

Go to the project directory

```bash
  cd auth-cial
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```

or

```bash
  python -m uvicorn main:app --reload --port <PORT TO RUN>
```

***Observation:** Use Python 3.10.0*


## 🟢 Running Tests

To run tests, run the following command

```bash
  npm run test
```


## 🟢 Authors

- [@ThiagoCAzevedo](https://www.github.com/thiagocazevedo)
- [@ThiagoCanatoAzevedo](https://www.github.com/thiagocanatoazevedo)


## 🟢 Support

For support, email nata.silva@gruposese.com or contact Sesé IT support.

