from django.urls import path
from . import views


urlpatterns = [


    path('api', views.apiOverview, name='api-overview'),

    # ------------ USER -------------
    path('user-list', views.userList, name='user-list'),
    path('user-detail/<str:pk>/', views.userDetail, name='user-detail'),
    path('user-create', views.createUser, name='user-create'),
    path('user-update', views.updateUser, name='user-update'),

    # ------------ EVENT -------------
    path('event-list', views.eventList, name='event-list'),
    path('event-detail/<str:pk>/', views.eventDetail, name='event-detail'),
    path('event-create', views.createEvent, name='event-create'),
    path('event-update/<str:pk>/', views.updateEvent, name='event-update'),
]

# {
#     "name": "OscaFest",
#     "description": "An Open Source Community Africa Festival",
#     "Location": "Lagos, Nigeria",
#     "Date": "December 25, 2020",
#     "Time": "12:00 pm",
#     "host": "Open Source Community Africa",
#     "guest": "starr"
# }

# {
#     "name": "partypal",
#     "version": "0.1.0",
#     "private": True,
#     "dependencies": {
#         "@testing-library/jest-dom": "^5.11.4",
#         "@testing-library/react": "^11.1.0",
#         "@testing-library/user-event": "^12.1.10",
#         "axios": "^0.21.0",
#         "bootstrap": "^4.5.3",
#         "react": "^17.0.1",
#         "react-bootstrap": "^1.4.0",
#         "react-dom": "^17.0.1",
#         "react-router-dom": "^5.2.0",
#         "react-scripts": "4.0.0",
#         "web-vitals": "^0.2.4"
#     },
#     "scripts": {
#         "start": "react-scripts start",
#         "build": "react-scripts build",
#         "test": "react-scripts test",
#         "eject": "react-scripts eject"
#     },
#     "eslintConfig": {
#         "extends": [
#             "react-app",
#             "react-app/jest"
#         ]
#     },
#     "browserslist": {
#         "production": [
#             ">0.2%",
#             "not dead",
#             "not op_mini all"

#         ],  
#         "development": [
#             "last 1 chrome version",
#             "last 1 firefox version",
#             "last 1 safari version"
#         ]
#     }
# }