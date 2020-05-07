package run.halo.app.filter;

import org.springframework.web.filter.OncePerRequestFilter;
import run.halo.app.service.OptionService;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class WrapRequestFilter extends OncePerRequestFilter {

    private static final String[] PATHS = new String[] { "/food", "/equipment" };
    private final OptionService optionService;

    public WrapRequestFilter(OptionService optionService) {
        this.optionService = optionService;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException, IOException, ServletException {
        ServletContextFacadeRequestWrapper wrapper = new ServletContextFacadeRequestWrapper(request);
        String path = getMatchingContextPathForRequest(request);
        if (path != null) {
            wrapper.setContextPath(request.getContextPath() + path);
            String newPath = request.getServletPath().substring(path.length());
            if (newPath.length() == 0) {
                newPath = "/";
            }
            wrapper.setServletPath(newPath);
        }
        filterChain.doFilter(wrapper, response);
    }

    public String getMatchingContextPathForRequest(HttpServletRequest request) {
        if (optionService.isEnabledAbsolutePath()) {
            String blogBaseUrl = optionService.getBlogBaseUrl();
            String contextPath = blogBaseUrl.substring(blogBaseUrl.indexOf("//") + 2);
            if(contextPath.indexOf("/") != -1) {
                contextPath = contextPath.substring(contextPath.indexOf("/"));
                if (request.getServletPath().startsWith(contextPath)) {
                    return contextPath;
                }
            }
        }

        return null;
    }

}