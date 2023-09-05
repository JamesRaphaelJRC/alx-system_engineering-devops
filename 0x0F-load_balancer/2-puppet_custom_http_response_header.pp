# Define Nginx class, installs nginx server and configures it

class { 'nginx':
	manage_repo => true,
}

class { 'nginx::package':
	ensure => 'installed',
}

file { '/var/www/html':
	ensure	=> 'directory',
	mode	=> '777',
}

file { '/var/www/html/index.html':
	ensure	=> 'present',
	content	=> "Hello World!",
}

file { '/var/www/html/404.html':
	ensure	=> 'present',
	content	=> "Ceci n'est pas une page\n",
}

file { '/etc/nginx/sites-available/default':
	ensure	=> 'present',
	content	=> "
server {
	listen 80;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm;
	add_header X-Served-By $HOSTNAME;

	location /redirect_me {
		return 301 http://google.com;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}
",
}

nginx::resource::vhost { 'default':
	ensure	=> 'present',
}

service { 'nginx':
	ensure	 => 'running',
	enable	 => true,
	subscribe => File['/etc/nginx/sites-available/default'],
}
