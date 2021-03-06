
# 2d Array Rotation
  Python generates & rotates counter clockwise the grid, angular shows the magic!.

[![2d Array Rotation](https://2d-array-rotation.com/static/images/matrix_rotation.jpg)](https://2d-array-rotation.com/)


#### Requirements
- Python 3.7 & up
- Virtual Environment (pipenv)
- Angular 4 & up

### Initial Setup
```
git clone git@github.com:briansanchez/2d-array-rotation.git
$ cd 2d-array-rotation
# activate pipenv
$ pipenv shell

# run django
$ cd django_2d_array
$ install -r requirements.txt
$ python manage.py migrate
# run django
$ python manage.py runserver

$ cd ..

#angular
cd angular_2d_array
npm install
#run angular
ng serve

```

#### Grid Creation
My approach is to divide the grid in 8 sections.

1. Top row
2. Top left side of the grid
3. Top middle side of the grid
4. Top right side of the grid
5. Bottom left side of the grid
6. Bottom middle side of the grid
7. Bottom right side of the grid
8. Bottom row

#### Grid Rotation
Let's use imaginary iframes.

1. Save the position of the coords for each iframe in an array.
2. Make a copy of each iframe and rotate the copy.
3. Using this formula: (n rotations / total_cells_in_frame) * total_cells_in_frame, we can find the number where the grid comes back to original position "for each iframe" because rotations could be 1 million, so optimization is also a must.
4. After n Rotations, display the grid using step 1 with coords rotated in step 2.


## Python exercises in TDD style

### How to run tests locally (Linux or Mac OS X)
Locally running the unit testing requires [pytest](http://pytest.org)

Then you can run the tests with:
```
$ pytest django_2d_array/app/tests.py
```

You can run a single test case like this:
```
$ pytest django_2d_array/app/tests.py -k 'test_6_x_6'
```

You can run multiple test cases with:
```
$ pytest django_2d_array/app/tests.py -k 'test_6_x_6 or test_10_x_2 or test_2_x_4'
```
 
