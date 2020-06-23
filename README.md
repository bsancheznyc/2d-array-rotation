
# 2d Array Rotation
  Python3 generates & rotates the grid, angular shows the magic!.

#### Requirements
- Python 3.7 & up
- Virtual Environment (pipenv)
- Angular 4 & up

### Initial Setup
```
git clone git@github.com:briansanchez/2d-array-rotation.git
cd 2d-array-rotation
# activate pipenv
pipenv shell
cd django_2d_array
install -r requirements.txt
python manage.py migrate
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
My idea is to divide using imaginary belts, divide and conquer, each belt should be treated in an exclusive way.

1. Save the position of the coords for each belt in array.
2. Make a copy of each belt and rotate the copy (figure it out the formula <sup>1</sup> to find the right number where the grid comes back to original position "for each belt") because rotations could be 1 million, so rotate.
3. Rotations done? ok now display the grid using step 1 with coords rotated in step 2.

<sup>1</sup> (n rotations / total_cells_in_frame) * total_cells_in_frame

