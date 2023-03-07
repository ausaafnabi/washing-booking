from django.forms import Form
from djago import forms
from slot.models import Booking

class BookingForm(form.Forms):
    def __init__(self):
        pass

class BookingForm(forms.ModelForm):
	Date = forms.IntegerField(label='',widget=forms.TextInput(attrs = {
			'class': 'form-control','placeholder':'Order ID' ,'aria-label':'OrderID' ,'aria-describedby':'order-id-addon'}))
	user = forms.IntegerField(label='',widget=forms.TextInput(attrs = {
			'class': 'form-control','placeholder':'Price' ,'aria-label':'Price' ,'aria-describedby':'order-id-addon'}))
	slot = forms.ModelChoiceField(queryset=None,label='',widget=forms.Select(attrs = {
			'class': 'form-control','placeholder':'Assigned Vendor' ,'aria-label':'Assigned Vendor' ,'aria-describedby':'vendor-addon'}))
	comment = forms.CharField(max_length=250, label='',widget=forms.Textarea(attrs = {
			'class': 'form-control','placeholder':'Comments' ,'aria-label':'Comments' ,'aria-describedby':'comment-addon'}))
	
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['assignedVendor'].queryset = VendorProfile.objects.all()
	
	class Meta:
		model = Orders
		fields = ('orderID','price','assignedVendor','packingSlip','comments')
			
	def save(self,commit=True):
		order_add = super().save(commit=False)
		order_add.eta = timezone.now() + datetime.timedelta(days=15)
		if commit:
			order_add.save()
		return order_add