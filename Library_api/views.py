from .models import Book
from .serializers import BookSerializer,BookCostomSerializer
from rest_framework import generics,status
from .utils import Response
from .serializers import BookSearchSerializer, BookDetailSerializer
class BookViewApi(generics.GenericAPIView):
    serializer_class = BookSerializer

    def get(self,request):
        try:
            book = Book.objects.all()
            serializer=BookSerializer(book,many=True)
            return Response(
                {
                    "success":True,
                    "message":"user record view successfully",
                    "data":serializer.data
                },status=status.HTTP_201_CREATED
            )
        except Book.DoesNotExist:
            return Response({"user not found"})
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": str(e),
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class BookCreateApi(generics.CreateAPIView):
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                {
                        "success": True,
                        "message": "book created successfully",
                        "data": serializer.data
                    }, status=status.HTTP_201_CREATED
                )
            return Response(
            {
                    "success": False,
                    "message": "book record not found",
                    "data": serializer.errors
                 }, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    "success":False,
                    "message":str(e),

                },status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BookCreate(generics.CreateAPIView):
    serializer_class = BookCostomSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = BookCostomSerializer(data=request.data)
            if serializer.is_valid():
                book = Book.objects.create(
                    name=serializer.validated_data['name'],
                    author=serializer.validated_data['author'],
                    published_year=serializer.validated_data['published_year'],
                )
                serializer.save()
                return Response({"success": True, "message": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UpdateBookApi(generics.UpdateAPIView):
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):
        try:
            print(args,kwargs)

            old_book = Book.objects.get(pk=kwargs['pk'])
            serializer = self.get_serializer(old_book, data=request.data)
            if serializer.is_valid():
                self.perform_update(serializer)
                return Response(
                    {
                        "success":True,
                        "message":"Book updated successfully",
                        "data":serializer.data,

                    },status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    "success":False,
                    "message":"book doesn't added",
                    "data":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "message":str(e)
                },status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class DeleteBookApi(generics.DestroyAPIView):
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(pk=kwargs['pk'])
            book.delete()
            return Response(
                {
                    "success":True,
                    "message":"Book Deleted Successfully",
                },status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "success":False,
                    "message":str(e),

                },status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




class BookSearchPostAPIView(generics.GenericAPIView):
    serializer_class = BookSearchSerializer

    def post(self, request):
        serializer = BookSearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        search_name = serializer.validated_data["name"]

        books = Book.objects.filter(name__icontains=search_name)

        if not books:
            return Response(
                {"success": False, "message": "No book found with that name", "data": []},
                status=status.HTTP_404_NOT_FOUND,
            )

        result_serializer = BookDetailSerializer(books, many=True)

        return Response(
            {
                "success": True,
                "message": "Books fetched successfully",
                "data": result_serializer.data
            },
            status=status.HTTP_200_OK
        )