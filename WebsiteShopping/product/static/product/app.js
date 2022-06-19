// // function addItemLocal()
// // {
// //     window.localStorage.setItem("YourCart", "aaaaaa");
// //     Cart = window.localStorage.getItem("YourCart");
// //     if (localStorage.getItem("YourCart") === null) {
// //         ItemCart = []
// //         ItemCart.append("sdsdsfdfdsfds")
// //         window.localStorage.setItem("YourCart", ItemCart);
// //     }
// //     else
// //     {
// //         Cart.append("sdsdsfdfdsfds")
// //         window.localStorage.setItem("YourCart", ItemCart);
// //     }
// //     // cart = localStorage.getItem("yourCart");
// //     // if(cart.length > 0)
// //     // {
// //     //     ItemCart.append("sdsdsfdfdsfds")
// //     //     window.localStorage.setItem("ItemCart", ItemCart);
// //     // }
// //     // else
// //     // {
// //     //     ItemCart = []
// //     //     ItemCart.append("sdsdsfdfdsfds")
// //     //     window.localStorage.setItem("ItemCart", ItemCart);
// //     // }
// // }

// function AddCart(id){
//     number = 1;
//     $.ajax({
//         type: 'POST',
//         url: "addCart/",
//         data: JSON.stringify({"id": id, "number": number, "csrfmiddlewaretoken": '{{csrf_token}}'}),
//         success: function (response) {
//             console.log(response);
//         },
//         error: function (response) {
//             console.log("sjshdsjdsajds");
//             alert(response["responseJSON"]["error"]);
//         }
//     })
// }
