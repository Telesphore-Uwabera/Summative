### UNIVERSITY RESIDENCE MANAGEMENT API - COMPREHENSIVE REPORT

### Project Overview

The University Residence Management API, built using Django REST Framework, is designed to manage buildings, rooms, and residents in university housing. It allows administrators to perform CRUD (Create, Read, Update, Delete) operations on these resources, ensuring smooth management of university housing facilities. The API is equipped with easy-to-read documentation generated by Swagger and Redoc, providing clear guidance for developers.

### API Functionality

Managing Buildings: Users can add, view, edit, and delete buildings.
Managing Rooms: Rooms are linked to specific buildings and can be managed through the API.
Managing Residents: Users can add, update, delete, and view residents in the university.
API Documentation: Swagger and Redoc offer detailed documentation with examples of requests and responses, facilitating easy API usage.
Overview of asynchronous programming
In asynchronous programming, some tasks can run on the background without hanging the main application. This technique is more relevant to long lasting operation which occupies the main application’s thread, such as network operations, file I/O or any other operation that could make the system hang. In Django, this is done with the help of Celery and background task management along with Django Channels for WebSocket operations.

### Identification of Asynchronous Tasks and Endpoints

To improve system performance and user experience, specific tasks within the API are handled asynchronously:
Sending Notifications (Emails/SMS):
Task: Sending email or SMS messages to residents.
Reason: Sending messages to many people can be time-consuming. Processing this task in the background ensures that the main task (e.g., adding a resident) finishes quickly without delay.

Data Syncing and Backups:
Task: Syncing resident information or creating backups.
Reason: Syncing large datasets or backing up data is resource-intensive. Asynchronous execution ensures these tasks don't slow down normal system operations.

Scheduling Maintenance:
Task: Scheduling regular maintenance for buildings or rooms.
Reason: Maintenance tasks can be complex and require processing time. Handling this in the background ensures the system remains responsive during scheduling.

Maintenance Requests:
Task: Processing maintenance requests, including assigning technicians, estimating costs, and sending notifications.
Reason: This task can run asynchronously, allowing residents to continue using the system while their request is processed in the background.

Room Booking:
Task: Allocating rooms involves checking availability, verifying payments, and updating records.
Reason: Asynchronous execution can process room bookings without blocking other operations, ensuring a smooth user experience.

Bulk Data Processing:
Task: Processing large uploads, such as importing resident data.
Reason: Asynchronous execution handles bulk uploads in the background, ensuring the system remains responsive during administrative tasks.

### Justification for Asynchronous Implementation
Asynchronous programming offers several advantages such as: The adoption of new technologies takes greater and greater restrictions off the advancement of the quality and coverage of production services.
Decreased Waiting Time For Operations that may Block User Action: Instead, if non-blocking operations are used then no such operation will hold up any operation on the user interface, and user can do their work while such long lasting operations will be done ‘behind the scenes’.
Enhanced Usage of the System: In such a mode, the system makes the response to more and more users and operations at the same time which increases the scalability of the system.
Effectiveness and Time-saving: The system reduces starving and waiting for a task as long as the response is therapeutic thanks to its management of performing notification, data processing tasks in the background grudging tasking. This results in efficiency and strength.

### Tools Used
Celery: For managing background tasks efficiently.
Redis: Used as the message broker for distributing background tasks.
Django Channels: For managing real-time, asynchronous WebSocket communication.

### Conclusion
Integrating asynchronous programming in the University Residence Management API enhances the system’s performance and user experience. By using Celery for background task management, tasks like notifications, data syncing, maintenance requests, and room bookings are processed without blocking other operations. This setup ensures that the API remains scalable, efficient, and responsive, catering to the complex needs of managing university housing.
Next steps include refining the asynchronous implementation, leveraging Django async views where applicable, and ensuring detailed API documentation with Swagger/Redoc for developers and users.
