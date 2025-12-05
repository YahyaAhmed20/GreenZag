from django.shortcuts import render


# Create your views here.


def about(request):


    return render(request, 'about/about.html')




# <section id="about" class="about">
#   <div class="container" data-aos="fade-up">
#     <div class="row position-relative">
#       <div class="col-lg-5 about-img" style="background-image: url({% static 'assets/img/about.jpg' %});"></div>
#       <div class="col-lg-7 ps-lg-5">
#         <h2>About Green Zag</h2>
#         <div class="our-story">
#           <h3>Who We Are</h3>
#           <p>
#             Green Zag is a professional engineering and contracting company established in the field of <strong>environmental technology</strong>. 
#             We specialize in providing end-to-end technological solutions for the design, construction, operation, and maintenance of water and wastewater treatment facilities for industrial clients and public authorities.
#           </p>
#           <p>
#             Our team comprises highly qualified engineers, chemists, technicians, and skilled laborers — all with extensive hands-on experience from major water and wastewater treatment organizations.
#           </p>
#           <ul class="list-unstyled mt-3">
#             <li class="d-flex align-items-start mb-2">
#               <span class="me-2 text-primary fs-5">💧</span> <!-- ✅ أيقونة -->
#               <span>Focus on sustainable, high-efficiency treatment systems</span>
#             </li>
#             <li class="d-flex align-items-start mb-2">
#               <span class="me-2 text-primary fs-5">🏆</span> <!-- ✅ أيقونة -->
#               <span>Proven track record in major regional projects</span>
#             </li>
#             <li class="d-flex align-items-start mb-2">
#               <span class="me-2 text-primary fs-5">🛠️</span> <!-- ✅ أيقونة -->
#               <span>Comprehensive after-sales and maintenance support</span>
#             </li>
#           </ul>
#         </div>
#       </div>
#     </div>
#   </div>
# </section>





# <section id="hero" class="hero">
#   <main id="main">

#     <div class="info d-flex align-items-center">
#       <div class="container">
#         <div class="row justify-content-center">
#           <div class="col-lg-6 text-center">
#             <h2 data-aos="fade-down">
#               Welcome to <span>Green Zag</span>
#             </h2>

#             <p data-aos="fade-up">
#               A leading engineering company specialized in water and wastewater treatment,
#               turnkey industrial solutions, and advanced environmental technologies for
#               municipalities and major industries.
#             </p>

#             <a data-aos="fade-up" data-aos-delay="200" href="#get-started" class="btn-get-started">
#               Discover More
#             </a>
#           </div>
#         </div>
#       </div>
#     </div>

#     <div id="hero-carousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">

#       <div class="carousel-item active" style="background-image: url({% static 'assets/img/hero-carousel/hero-carousel-1.jpg' %})">
#       </div>
#       <div class="carousel-item" style="background-image: url({% static 'assets/img/hero-carousel/p1.jpg' %})"></div>
#       <div class="carousel-item" style="background-image: url({% static 'assets/img/hero-carousel/p2.jpg' %})"></div>
#       <div class="carousel-item" style="background-image: url({% static 'assets/img/hero-carousel/hero-carousel-4.jpg' %})"></div>
#       <div class="carousel-item" style="background-image: url({% static 'assets/img/hero-carousel/hero-carousel-5.jpg' %})"></div>

#       <a class="carousel-control-prev" href="#hero-carousel" role="button" data-bs-slide="prev">
#         <span class="carousel-control-prev-icon bi bi-chevron-left" aria-hidden="true"></span>
#       </a>

#       <a class="carousel-control-next" href="#hero-carousel" role="button" data-bs-slide="next">
#         <span class="carousel-control-next-icon bi bi-chevron-right" aria-hidden="true"></span>
#       </a>

#     </div>

#   </main>
# </section>