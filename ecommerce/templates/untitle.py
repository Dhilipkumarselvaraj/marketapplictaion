customer_uuid
pm_id
first_name
second_name
email_id
mobile_no_primary
mobile_no_secondary
customer_type
period
quantity
supplier_name
date_of_join
area_code
address



customer_uuid = customer_uuid,
pm_id = pm_id,
first_name = first_name,
second_name = second_name,
email_id = email_id,
mobile_no_primary = mobile_no_primary,
mobile_no_secondary = mobile_no_secondary,
customer_type = customer_type,
period = period,
quantity = quantity,
supplier_name = supplier_name,
date_of_join = date_of_join,
area_code = area_code,
address = address,




<th id="customer_uuid">customer_uuid</th>




<!-- <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{% block title %}#PM{% endblock %}</title>
  </head>
  <body>
    <header>
      <h1>Base Page</h1>
      {% if user.is_authenticated %}
        <a href="{% url 'logout' %}">logout</a>
      {% else %}
        <a href="{% url 'login' %}">login</a> / <a href="{% url 'signup' %}">signup</a>
      {% endif %}
      <hr>
    </header>
    <main>
      {% block content %}
      {% endblock %}
    </main>
  </body>
</html> -->