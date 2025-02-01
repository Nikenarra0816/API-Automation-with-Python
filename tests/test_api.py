import requests

# The base URL for the API to be tested.
BASE_URL = "https://jsonplaceholder.typicode.com"


# Test case for a GET request to retrieve the list of posts.
def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    
    # Check if the response status code is 200 OK.
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check if the response body contains a list of posts.
    assert isinstance(response.json(), list), "Response body should be a list"
    
    # Check the length of the list (if needed).
    assert len(response.json()) > 0, "Posts list should not be empty"
    
    # Check that the first post contains the expected keys.
    first_post = response.json()[0]
    assert "id" in first_post, "Post should have an id"
    assert "title" in first_post, "Post should have a title"
    assert "body" in first_post, "Post should have a body"


# Test case for a GET request to retrieve a single post.
def test_get_single_post():
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    
    # Check if the response status code is 200 OK.
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check if the response body contains the post data.
    post = response.json()
    assert "id" in post, "Post should have an id"
    assert post["id"] == post_id, f"Expected post id {post_id}, got {post['id']}"


# Test case for a POST request to create a new post.
def test_create_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    
    # Check if the response status code is 201 Created.
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    # Check if the response body contains the newly created post data.
    created_post = response.json()
    assert "id" in created_post, "Created post should have an id"
    assert created_post["title"] == new_post["title"], f"Expected title {new_post['title']}, got {created_post['title']}"
    assert created_post["body"] == new_post["body"], f"Expected body {new_post['body']}, got {created_post['body']}"



def test_delete_post():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    
    # Check if the response status code is 200 OK (indicating the server accepted the deletion).
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check if the post is actually deleted by attempting to retrieve the post again.
    # JSONPlaceholder might not permanently delete the post, so we check for the status code 200 instead of 404.
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    
    # Check if the post still exists by expecting a 200 response (since JSONPlaceholder doesn't permanently delete data).
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Optionally, verify that the post data has not been changed after deletion.
    post = response.json()
    assert post["id"] == post_id, "Post ID should match"
    assert "title" in post, "Post should have a title"
    assert "body" in post, "Post should have a body"
