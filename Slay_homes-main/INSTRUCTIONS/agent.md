You are an expert full-stack cloud deployment engineer.
Your task is to fully migrate my existing website database from my local MySQL Workbench setup to TiDB Cloud and ensure the entire application works correctly when deployed on Render.
I do NOT want partial work, placeholders, assumptions, or simplified examples. I want production-ready implementation.
You must carefully analyze the existing project structure, backend code, database models, API routes, authentication logic, and all SQL interactions before making changes.
The final system must:
* Work correctly on Render hosting.
* Use TiDB Cloud as the production database.
* Preserve all existing website functionality.
* Avoid breaking animations, frontend UI, or existing business logic.
* Support future scaling.
* Handle production environment variables properly.
* Prevent database connection crashes.
* Properly create every table, relationship, constraint, and index.
* Work with real production traffic.

EXISTING DATABASE DETAILS
Use these TiDB credentials:
HOST: gateway01.ap-southeast-1.prod.aws.tidbcloud.com
PORT: 4000
DATABASE: sys
USERNAME: 31PQA6ccbXZVYGy.root
PASSWORD: wDFsSCk31FnCHjnC
SSL CA CERT PATH: /etc/ssl/cert.pem
IMPORTANT: TiDB requires SSL connection. Do NOT skip SSL configuration.

PRIMARY OBJECTIVES
You must complete ALL of the following tasks:
1. Analyze the entire project.
2. Detect the current backend framework automatically.
3. Detect the database technology currently used.
4. Detect ORM or raw SQL usage.
5. Replace local database configuration with TiDB configuration.
6. Convert all environment variables correctly.
7. Create production-ready database connection pooling.
8. Ensure Render deployment compatibility.
9. Ensure all tables are created properly.
10. Ensure migrations run correctly.
11. Ensure relationships and foreign keys are preserved.
12. Ensure authentication still works.
13. Ensure CRUD operations still work.
14. Ensure uploads/forms/admin panels still work.
15. Ensure deployment logs show no DB errors.
16. Ensure SSL is configured correctly.
17. Prevent connection timeout issues.
18. Prevent "Too many connections" issues.
19. Prevent CORS issues.
20. Prevent Render cold-start failures.
21. Ensure all API endpoints use the cloud database.
22. Remove any localhost-only configuration.
23. Ensure production-safe error handling.
24. Ensure automatic reconnect logic exists.
25. Ensure database queries are optimized.
26. Ensure indexes exist on important columns.
27. Ensure timestamps/default values work properly.
28. Ensure UTF-8 encoding support.
29. Ensure transactional integrity.
30. Ensure schema consistency.

STEP-BY-STEP IMPLEMENTATION REQUIREMENTS
STEP 1 — ANALYZE THE ENTIRE PROJECT
First:
* Scan all project files.
* Detect:
    * Backend framework
    * Frontend framework
    * ORM
    * SQL drivers
    * Environment variable usage
    * Existing database schema
    * Deployment configuration
    * Authentication system
    * Session handling
    * File uploads
    * API routes
    * Middleware
    * Render configuration
Then explain:
* Current architecture
* Weak points
* Required migration changes
* Possible deployment risks
Do NOT modify files blindly.

STEP 2 — BACKUP CURRENT DATABASE STRUCTURE
Generate:
* Full schema backup
* SQL dump
* Table creation scripts
* Foreign key mapping
* Constraints mapping
* Index mapping
Ensure nothing is lost.

STEP 3 — CONFIGURE TIDB CLOUD CONNECTION
Replace ALL local DB connections.
Detect whether the project uses:
* mysql2
* Sequelize
* Prisma
* TypeORM
* Knex
* Django ORM
* SQLAlchemy
* JDBC
* PHP PDO
* Raw MySQL
* Any other database library
Then configure TiDB correctly.
IMPORTANT REQUIREMENTS:
* Use SSL.
* Use environment variables.
* Never hardcode secrets.
* Add retry logic.
* Add pooling.
* Add production-safe timeouts.
* Add graceful connection recovery.
Example logic requirements:
* Pool connection limit
* Idle timeout
* Queue limit
* Auto reconnect
* Error logging

STEP 4 — CREATE PRODUCTION ENVIRONMENT VARIABLES
Create proper Render-compatible environment variables.
Generate:
DB_HOST= DB_PORT= DB_NAME= DB_USER= DB_PASSWORD= DATABASE_URL= NODE_ENV=production
If framework-specific variables are required:
* Generate them.
* Explain where to place them.
Ensure secrets are NOT exposed publicly.

STEP 5 — DATABASE MIGRATION
VERY IMPORTANT: ALL tables must be recreated correctly.
Requirements:
* Create every table.
* Preserve all columns.
* Preserve data types.
* Preserve AUTO_INCREMENT behavior.
* Preserve primary keys.
* Preserve foreign keys.
* Preserve cascading behavior.
* Preserve NOT NULL constraints.
* Preserve unique constraints.
* Preserve indexes.
* Preserve timestamps.
* Preserve enums.
* Preserve defaults.
* Preserve relationships.
* Preserve many-to-many mappings.
Do NOT simplify schemas. Do NOT skip any table. Do NOT remove constraints.

STEP 6 — VERIFY TIDB COMPATIBILITY
TiDB behaves similarly to MySQL but has differences.
Check for:
* Unsupported SQL syntax
* Engine-specific features
* Locking issues
* Stored procedure incompatibilities
* Trigger incompatibilities
* Transaction issues
* Strict mode issues
* Unsupported indexing patterns
Automatically fix incompatibilities.

STEP 7 — DATA MIGRATION
If existing local data exists:
* Export it.
* Transform it if necessary.
* Import it into TiDB.
* Validate row counts.
* Validate integrity.
Check:
* Orphan rows
* Broken foreign keys
* Encoding problems
* Duplicate constraints
* NULL violations

STEP 8 — UPDATE APPLICATION CODE
Update all backend logic to use TiDB.
Requirements:
* Update all database imports.
* Update all query connections.
* Update all transaction handling.
* Update ORM configurations.
* Update migration configs.
* Update deployment configs.
* Update seeders.
* Update session storage.
* Update authentication storage.
* Update admin functionality.
* Update user functionality.
Ensure no localhost references remain.

STEP 9 — RENDER DEPLOYMENT CONFIGURATION
Prepare the project specifically for Render.
Requirements:
* Correct build commands.
* Correct start commands.
* Correct environment variables.
* Production mode enabled.
* Proper port binding.
* Health check compatibility.
* Persistent connection handling.
* Static file serving compatibility.
* Correct CORS configuration.
* Correct HTTPS handling.
Generate:
* render.yaml if needed
* Deployment instructions
* Environment variable setup guide

STEP 10 — CREATE DATABASE INITIALIZATION LOGIC
When deployed on Render:
* App should automatically verify database connection.
* App should automatically create tables if missing.
* App should automatically run migrations.
* App should fail gracefully.
* App should show meaningful logs.
Do NOT allow silent failures.

STEP 11 — VALIDATION TESTING
Test ALL major features:
* Registration
* Login
* Logout
* CRUD operations
* Admin operations
* File uploads
* Search
* Filtering
* API routes
* Sessions
* Password hashing
* Role management
* Data persistence
* Form submissions
* Database writes
* Database reads
* Database updates
* Database deletes
Verify:
* No broken queries.
* No connection leaks.
* No async failures.
* No deployment crashes.

STEP 12 — OPTIMIZATION
Optimize:
* Query performance
* Indexing
* Lazy loading
* Pagination
* Connection pooling
* Transaction usage
* Error handling
* Logging
* Security
Add indexes where necessary.

STEP 13 — SECURITY HARDENING
Implement:
* SQL injection prevention
* Environment variable protection
* Secure authentication handling
* Input validation
* Rate limiting if applicable
* Production-safe error messages
* Secure cookie/session settings
* HTTPS-safe configuration

STEP 14 — FINAL OUTPUT REQUIREMENTS
At the end provide:
1. Updated project structure
2. Updated database configuration
3. Full migration scripts
4. All changed files
5. Render deployment steps
6. Environment variable setup guide
7. Database verification steps
8. Rollback instructions
9. Troubleshooting guide
10. Performance recommendations
11. Security recommendations
12. Production deployment checklist

IMPORTANT RULES
* Do NOT delete existing functionality.
* Do NOT simplify the database.
* Do NOT skip relationships.
* Do NOT use mock code.
* Do NOT leave TODO placeholders.
* Do NOT assume missing details.
* Analyze before modifying.
* Preserve frontend behavior.
* Ensure production readiness.
* Ensure Render compatibility.
* Ensure TiDB compatibility.
* Ensure scalability.
* Ensure maintainability.
* Ensure reliability.

EXPECTED RESULT
After implementation:
* Website should run perfectly on Render.
* TiDB Cloud should act as the primary production database.
* All tables should exist correctly.
* All CRUD operations should work.
* Authentication should work.
* Admin functionality should work.
* No localhost dependency should remain.
* Database should persist permanently.
* Deployment should be stable.
* No database connection failures should occur.
* Production deployment should be clean and scalable.








