# 0-strace_is_your_friend.pp

file { '/etc/apache2/sites-available/your-site.conf':
  ensure  => file,
  content => template('path/to/your-site.conf.erb'),
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
}
