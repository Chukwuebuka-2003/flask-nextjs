from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy database to store registered users
registered_users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    name = data.get('name')
    department = data.get('department')
    profile = data.get('profile')
    password = data.get('password')

    # Check if all required fields are present
    if not all([name, department, profile, password]):
        return jsonify({'message': 'Missing required fields'}), 400

    # Get profile image file
    profile_image = request.files.get('profileImage')

    # Process profile image if provided
    if profile_image:
        # Save the profile image to a desired location
        profile_image_path = f"uploads/{profile_image.filename}"
        profile_image.save(profile_image_path)
    else:
        profile_image_path = None

    # Add user to the database
    registered_users.append({
        'name': name,
        'department': department,
        'profile': profile,
        'password': password,
        'profile_image': profile_image_path
    })

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/')
def show_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
