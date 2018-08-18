import os
import shutil

makefile = os.path.join(os.getcwd(), 'Makefile')
makefile_destination = os.path.join(os.getcwd(), '../', 'Makefile')

lower_makefile_destination = os.path.join('/'.join(makefile_destination.split('/')[:-3]), makefile_destination.split('/')[-1:][0].lower())

if os.path.exists(makefile_destination) is True or  \
   os.path.exists(os.path.join(lower_makefile_destination)) is True:
    with open(makefile, 'r') as f:
        make_content = f.read()
    if make_content:
        print('**' * 32)
        print('It looks like you already have a Makefile')
        print('Please, add these items to your existing makefile')
        print('**' * 32)
        print('')
        print(make_content)
else:
    shutil.copy2(makefile, makefile_destination)
    print('Done.')
