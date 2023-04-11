try:
    import csv
    try:
        from flask import Flask, render_template, request, send_file
    except ImportError:
        import os
        print('Requirements isn\'t installed, installing now.')
        ret_code = os.system('pip3 install -r requirements.txt')
        if(ret_code != 0):
            print('Requirements installation failed.')
            quit()
        print('Requirements has been installed, restart me!')
        quit()
except ImportError:
    print('This development isn\'t compatible with python2. Use python > 3.4 to run.')
    quit()
runtime = 0

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def form():
    global runtime
    if request.method == 'POST':
        col1 = request.form.get('col1')
        col2 = request.form.get('col2')
        col3 = request.form.get('col3')
        col4 = request.form.get('col4')
        col5 = request.form.get('col5')
        col6 = request.form.get('col6')
        col7 = request.form.get('col7')
        col8 = request.form.get('col8')
        col9 = request.form.get('col9')
        col10 = request.form.get('col10')
        col11 = request.form.get('col11')
        col12 = request.form.get('col12')
        col13 = request.form.get('col13')
        col14 = request.form.get('col14')
        col15 = request.form.get('col15')
        col16 = request.form.get('col16')
        col17 = request.form.get('col17')
        col18 = request.form.get('col18')
        # need repeat for the other columns
        with open('data'+str(runtime)+'.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name: ", col1])
            writer.writerow(["Surname: ", col2])
            writer.writerow(["Age: ", col3])
            writer.writerow(["Country: ", col4])
            writer.writerow(["Race: ", col5])
            writer.writerow(["Gender: ", col6])
            writer.writerow(["Address: ", col7])
            writer.writerow(["Phone Number: ", col8])
            writer.writerow(["Birthday: ", col9])
            writer.writerow(["E-mail Address: ", col10])
            writer.writerow(["Website: ", col11])
            writer.writerow(["Mother Name: ", col12])
            writer.writerow(["Father Name: ", col13])
            writer.writerow(["Height: ", col14])
            writer.writerow(["Weight: ", col15])
            writer.writerow(["Vehicle: ", col16])
            writer.writerow(["Favorite Color: ", col17])
            writer.writerow(["Pet: ", col18])
            runtime+=1
        return 'Form submitted successfully and data written to CSV file!'
    return render_template('form.html')

#@app.route('/bg')
#def bg():
#    filename = 'wallpaper.png'
#    return send_file(filename, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug=False) #make false before production

