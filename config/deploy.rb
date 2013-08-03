set :application, "lightcastle_site"
set :repository,  "git@github.com:lightcastle/djangowebsite.git"
set :scm, :git
set :user, "lc_web_user"
set :deploy_to, "/home/lc_web_user/lightcastletech.com"
set :ssh_options, { :forward_agent => true }
set :deploy_via, :remote_cache
server "54.243.182.84",   :web, :app, :db, :primary => true
set :normalize_asset_timestamps, false


#
#
#cp /home/lc_web_user/lightcastletech.com/settings.py /home/lc_web_user/lightcastletech.com/current/lightcastle/lightcastle/settings.py"
#    run "ln -nfs #{shared_path}/public/images/posts #{release_path}/public/images/posts"
  end
end



# set :scm, :git # You can set :scm explicitly or Capistrano will make an intelligent guess based on known version control directory names
# Or: `accurev`, `bzr`, `cvs`, `darcs`, `git`, `mercurial`, `perforce`, `subversion` or `none`

#role :web, "Apache"                          # Your HTTP server, Apache/etc
#role :app, "Apache"                          # This may be the same as your `Web` server
#role :db,  "mysql", :primary => true # This is where Rails migrations will run
#role :db,  ""

# if you want to clean up old releases on each deploy uncomment this:
# after "deploy:restart", "deploy:cleanup"

# if you're still using the script/reaper helper you will need
# these http://github.com/rails/irs_process_scripts

# If you are using Passenger mod_rails uncomment this:
# namespace :deploy do
#   task :start do ; end
#   task :stop do ; end
#   task :restart, :roles => :app, :except => { :no_release => true } do
#     run "#{try_sudo} touch #{File.join(current_path,'tmp','restart.txt')}"
#   end
# end
