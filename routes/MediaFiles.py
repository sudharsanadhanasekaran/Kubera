from flask import Blueprint,request,jsonify
from model import *
MediaFiles_blueprint=Blueprint("MediaFiles_blueprint",__name__)
@MediaFiles_blueprint.route('/media',methods=['POST'])
def create_media():
        data=request.json
        create_user=MediaFiles(
            user_id=data.get('user_id'),
            vendorId=data.get('vendorId'),
            file_name=data['file_name'],
            file_url=data['file_url'],
            file_title=data.get('file_title'),
            file_type=data['file_type'],
            alt_text=data.get('alt_text'),
            entity_type=data['entity_type'],
            entity_id=data['entity_id'])
        db.session.add(create_user)
        db.session.commit()
        return jsonify({"message":"Media created successfully",
                           "data":create_user.to_dict()
                           })
#-----Get all media---
@MediaFiles_blueprint.route('/media',methods=['GET'])
def get_all_media():
    get_media=MediaFiles.query.all()
    result = []
    for media in get_media:
        result.append(media.to_dict())
    return jsonify(result)    
#----get by media id---
@MediaFiles_blueprint.route("/media/<int:id>", methods=["GET"])
def get_media(id):
    user = MediaFiles.query.get(id)
    # if not user or user.delete_status:
    #     return jsonify({"message": "User not found"})
    return jsonify(user.to_dict())
#-----update media----
@MediaFiles_blueprint.route('/media/<int:id>', methods=['PUT'])
def update_media(id):
    media = MediaFiles.query.get(id)
    if not media:
        return jsonify({"message": "Media not found"}), 404
    data = request.get_json()
    media.user_id = data.get('user_id', media.user_id)
    media.vendorId = data.get('vendorId', media.vendorId)
    media.file_name = data.get('file_name', media.file_name)
    media.file_url = data.get('file_url', media.file_url)
    media.file_title = data.get('file_title', media.file_title)
    media.file_type = data.get('file_type', media.file_type)
    media.alt_text = data.get('alt_text', media.alt_text)
    media.entity_type = data.get('entity_type', media.entity_type)
    media.entity_id = data.get('entity_id', media.entity_id)
    db.session.commit()
    return jsonify({
        "message": "Media updated successfully",
        "data": media.to_dict()
    })
#-------- delete media--------
@MediaFiles_blueprint.route("/media/<int:id>/delete",methods=['PUT'])
def delete_media(id):
    user = MediaFiles.query.get(id)
    if not user or user.delete_status:
        return jsonify({"message": "User not found"}), 404
    user.delete_status = True
    db.session.commit()
    return jsonify({
        "message": "User deleted successfully",
        "delete_status": user.delete_status
    })
    
    '''Postman API Body data
    {
            "user_id":9,
            "vendorId":107,
            "file_name":"image9.jpg",
            "file_url":"https://example.com/uploads/image7.jpg",
            "file_title":"Product Image9",
            "file_type":"image9/jpeg",
            "alt_text":"back view of product",
            "entity_type":"product",
            "entity_id":19
}'''