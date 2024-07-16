from django.db import models

class UseCases(models.Model):
    use_case = models.CharField(max_length=200)
    description = models.TextField()
    benefits = models.TextField()

    def __str__(self):
        return self.use_case
    
    class Meta:
        verbose_name_plural = "Use cases"
    
class BusinessValue(models.Model):
    business_dimension = models.CharField(max_length=200)
    description = models.TextField()
    ponderation = models.FloatField()

    def __str__(self):
        return self.business_dimension
    
    class Meta:
        verbose_name_plural = "Business Value"
    
class BusinessCalifications(models.Model):
    contribution = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.contribution  
    
    class Meta:
        verbose_name_plural = "Business Califications"
    
class Feasibility(models.Model):
    feasibility = models.CharField(max_length=200)
    description = models.TextField()
    ponderation = models.FloatField()

    def __str__(self):
        return self.feasibility  
    
    class Meta:
        verbose_name_plural = "Feasibility"
    
class FeasibilityCalifications(models.Model):
    contribution = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.contribution
    
    class Meta:
        verbose_name_plural = "Feasibility Califications"