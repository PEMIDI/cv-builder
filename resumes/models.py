from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _

from utils.models import BaseModel

User = get_user_model()


class Skill(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='skills', on_delete=models.CASCADE)
    title = models.CharField(max_length=32, verbose_name=_('title'))
    rate = models.PositiveSmallIntegerField(verbose_name=_('rate'),
                                            validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')
        db_table = 'Skill'
        ordering = ('title',)

    def __str__(self):
        return f"{self.user} - {self.title}"


class Education(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='educations', on_delete=models.CASCADE)
    institution = models.CharField(max_length=64, verbose_name=_('institution'))
    degree = models.CharField(max_length=32, verbose_name=_('degree'))
    start_date = models.DateField(verbose_name=_('start date'))
    end_date = models.DateField(verbose_name=_('end date'), null=True, blank=True)

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')
        db_table = 'Education'
        ordering = ('start_date',)

    def __str__(self):
        return f"{self.institution} > {self.start_date} - {self.end_date}"

    def clean(self):
        if self.end_date and self.start_date > self.end_date:
            raise ValidationError("Start date must be before the end date")

    def is_graduated(self):
        return self.end_date is not None


class Certificate(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='certificates', on_delete=models.CASCADE)
    issuing_authority = models.CharField(max_length=32, verbose_name=_('issuing authority'))
    issue_date = models.DateField(verbose_name=_('issue date'))

    class Meta:
        verbose_name = _('certificate')
        verbose_name_plural = _('certificates')
        ordering = ('-issue_date',)


class Experience(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=32, verbose_name=_('company'))
    position = models.CharField(max_length=32, verbose_name='position')
    start_date = models.DateField(verbose_name=_('start date'))
    end_date = models.DateField(verbose_name=_('end date'), null=True)
    description = models.CharField(max_length=500, verbose_name=_('description'))

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')
        db_table = 'Experience'
        ordering = ('-start_date',)

    def __str__(self):
        return f"{self.user} - {self.company}"

    def clean(self):
        if self.end_date and self.start_date > self.end_date:
            raise ValidationError("Start date must be before the end date")

    def is_present(self):
        return self.end_date is not None


class Bio(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Bio')
        db_table = 'Bio'
