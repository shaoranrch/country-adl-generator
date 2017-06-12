#
#Generated at: {{ build_time }}
#
#{{ comments }}
#
/ip firewall address-list 
{% for network in adl -%}
add list="{{ list_name }}" address="{{ network }}"
{% endfor %}
