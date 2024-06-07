from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.response import Response

# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status" : f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data, status=status.HTTP_200_OK)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):

    # def get(self, request, pk):
    #    try:
    #        book = Book.objects.get(id=pk)
    #        serializer_data = BookSerializer(book).data
    #
    #        data = {
    #            "status": "Successfull",
    #            "book": serializer_data
    #        }
    #        return Response(data, status=status.HTTP_200_OK)
    #    except Book.DoesNotExist:
    #        data = {
    #            "status": "Error",
    #            "message": "Book not found."
    #        }
    #        return Response(data, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer_data = BookSerializer(book).data
        data = {
            "status":"Successfull",
            "books":serializer_data
        }
        return Response(data, status=status.HTTP_200_OK)
# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):

    # def delete(self, request, pk):
    #     try:
    #         book = Book.objects.get(id=pk)
    #         book.delete()
    #         return Response({
    #             "status":True,
    #             "message":"Successfull"
    #         }, status=status.HTTP_204_NO_CONTENT)
    #
    #     except Book.DoesNotExist:
    #         return Response({
    #             "status":"Error",
    #             "message":"Book not found"
    #         }, status=status.HTTP_404_NOT_FOUND)
    #
    #
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):

    def put(self, request, pk):
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(instance=book, data=request.data, partial=True)
            if serializer.is_valid():
                book_saved = serializer.save()
                data = {
                    "status": True,
                    "message": f"Book {book_saved} update succesfull",
                    "books": serializer
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response({
                "Status":"Errors",
                "message":"Book not found",
                "errors":serializer.errors
            }, status=status.HTTP_404_NOT_FOUND)
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":"Book are saved to the database",
                "books":data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        else:
            data = {
                "status":"Error",
                "message":"Book could not be saved ",
                "errors":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


# class BookListCreateApiView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListCreateApiView(APIView):

    def get(self,request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data

        data = {
            "status":f"Returned {len(books)} books",
            "message":"Successfull",
            "books":serializer_data
        }
        return Response(data, status=status.HTTP_200_OK)
    def post(self,request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":"Book are saved to the databas",
                "books":data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "status":"Error",
                "messages":"Book could not be saved",
                "errors":serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
# class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateDeleteApiView(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer_data = BookSerializer(book).data
        data = {
            "status":"Successfull",
            "books":serializer_data
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            book_saved = serializer.save()
            data = {
                "status": True,
                "message": f"Book {book_saved} update succesfull",
                "books": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({
            "Status": "Errors",
            "message": "Book not found",
            "errors": serializer.errors
        }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({
            "status":"Successfull delete",
            "message":"Delete book"
        }, status=status.HTTP_204_NO_CONTENT)

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer