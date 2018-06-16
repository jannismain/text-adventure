gifs: docs/*.mov
docs/*.mov:
	sh -c '. print $(@)'
	print $(@F)
	sh -c '. ffmpeg -i $(@) -pix_fmt rgb24 -r 10 $(@F).gif'

gifs:
	ffmpeg -i docs/screencap.mov -r 10 docs/screencap.gif

optimize:
	convert -layers Optimize docs/screencap.gif docs/screencap_opt.gif