# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackSerializer(many=True, read_only=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']

#     def create(self, validated_data):
#         tracks_data = validated_data.pop('tracks')
#         album = Album.objects.create(**validated_data)
#         for track_data in tracks_data:
#             Track.objects.create(album=album, **track_data)
#         return album