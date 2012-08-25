backend default {
    .host = "127.0.0.1";
    .port = "5000";
}

sub vcl_fetch {
  if (req.url == "/") {
    set beresp.ttl = 5 m;
    set beresp.do_esi = true;
  } 
}
