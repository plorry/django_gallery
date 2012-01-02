from andrewgardner.blog.models import Gallery
from django.utils import simplejson
from django.http import Http404, HttpResponse

def get_image(request):
	get = request.GET
	if request.is_ajax():
		gallery_id = get['gallery_id']
		gallery_id = int(gallery_id.lstrip('gallery_'))
		index = get['index']
		try:
			index_val = index.find('image_')
			index = int(index[index_val + 6:]) - 1
		except:
			index = int(index)

		gallery = Gallery.objects.get(id = gallery_id)
		if (index)  >= len(gallery.images.all()):
			index = 0
		image = gallery.images.all()[index]

		image_url = image.image.url
		caption = image.text
		
		response_dict = { 'image':image_url, 'caption':caption, 'index':index + 1, 'gallery_id':gallery_id }
		return HttpResponse(simplejson.dumps(response_dict))
	else:
		raise Http404