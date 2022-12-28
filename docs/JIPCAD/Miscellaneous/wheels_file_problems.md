Center of one sphere: assumed to be (0,0,0)
center of other spehre: assumed to be (0,3,3)

JIPCAD problems:
Seemingly difficult to find the centers of the rectangles. 
```html
point big_rec_1 (-3 -6 0) endpoint
point big_rec_2 (3 -6 0) endpoint
point big_rec_3 (3 3 0) endpoint
point big_rec_4 (-3 3 0) endpoint
```


```html
point bigger_rec_1 (-3 -9 0) endpoint
point bigger_rec_2 (3 -9 0) endpoint
point bigger_rec_3 (3 3 0) endpoint
point bigger_rec_4 (-3 3 0) endpoint
```

For some reasons these two pairs of crosssectional points have the same center point
```html
point scenter_rec_1 (-0.8 -3 0) endpoint
point scenter_rec_2 (0.8 -3 0) endpoint
point scenter_rec_3 (0.8 0 0) endpoint
point scenter_rec_4 (-0.8 0 0) endpoint
```

And this is the head part below, and for some reason this also doesnt work:
```html
point lcenter_rec_1 (-3 -5 0) endpoint
point lcenter_rec_2 (3 -5 0) endpoint
point lcenter_rec_3 (3 2 0) endpoint
point lcenter_rec_4 (-3 2 0) endpoint
```
And for some reason this doesn't center either, but the interesting thing is the base rectangle has coordinates:
```html
point big_rec_1 (-3 -6 0) endpoint
point big_rec_2 (3 -6 0) endpoint
point big_rec_3 (3 3 0) endpoint
point big_rec_4 (-3 3 0) endpoint
```
but for some reason this works

![[Zoom_uoZIawaPwZ.png]]
This is also the merge thing, which doesn't works



