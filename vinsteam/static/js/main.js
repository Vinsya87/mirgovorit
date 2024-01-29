// $(document).ready(function() {
//     $('#id_products-TOTAL_FORMS').attr('type', 'hidden');

//     $(document).on('input', '[id^="id_products-"][id$="-product_name"]', function() {
//         var query = $(this).val();
//         var formPrefix = $(this).attr('name').split('-')[1];

//         $.ajax({
//             url: '/product_search/',
//             method: 'GET',
//             data: {'query': query},
//             dataType: 'json',
//             success: function(data) {
//                 var resultsDiv = $('#id_products-' + formPrefix + '-product_results');
//                 resultsDiv.html('');

//                 data.results.forEach(function(product) {
//                     resultsDiv.append('<div>' + product.name + '</div>');
//                 });
//             },
//             error: function(xhr, status, error) {
//                 console.error(error);
//             }
//         });
//     });
// });

  
  
  
