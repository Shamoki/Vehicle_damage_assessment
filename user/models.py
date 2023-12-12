from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    # Link the assessment to the user who created it
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # A field for the image of the vehicle (ensure you have Pillow installed for ImageField)
    image = models.ImageField(upload_to='vehicle_images/')
    
    # A field for any additional information the user might provide about the damage
    description = models.TextField()
    
    # A field for the assessment result (e.g., cost estimate, damage severity) 
    # that will be filled out after processing by the ML model
    result = models.TextField(blank=True)
    
    # Timestamps for the assessment
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Assessment for {self.user.username} at {self.created_at}'
    
class VehicleReport(models.Model):
    # A foreign key which links each report to a specific user. This assumes that a report belongs to one user.
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle_reports')
    
    # The basic details about the vehicle report
    title = models.CharField(max_length=200)  # The title of the report
    description = models.TextField()  # The detailed description of the issue
    date_submitted = models.DateTimeField(auto_now_add=True)  # The date and time the report was created
    
    # If there are any specific details about the vehicle you want to record, you might add them here
    vehicle_make = models.CharField(max_length=100)  # e.g., "Honda", "Toyota", etc.
    vehicle_model = models.CharField(max_length=100)  # e.g., "Accord", "Camry", etc.
    vehicle_year = models.IntegerField()  # e.g., 2005, 2012, etc.

    # ... any other fields that are relevant to a vehicle report ...

    def __str__(self):
        return self.title  # A string representation of the report, change to suit your preference
