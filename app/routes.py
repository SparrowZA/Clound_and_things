import json
from flask import Blueprint, Response, jsonify, request
from usecases.combine_intervals import combine_intervals_usecase

blueprint = Blueprint("intervals", __name__)

@blueprint.route("/intervals", methods=["GET"])
def combine_intervals():
    # This should be a post method. That takes a list of
    # intervals and returns them after manipulating them
    result = combine_intervals_usecase([])

    return Response(
        json.dumps(result),
        mimetype="application/json",
        status=200
    )
