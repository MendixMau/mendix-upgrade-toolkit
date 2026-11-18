package shopkit.impl;

import com.mendix.core.Core;
import com.mendix.systemwideinterfaces.core.IContext;

// Marketplace module code: the plan updates ShopKit, which replaces this file
public class Query {
	static long count(IContext c, String xp) throws Exception { return Core.retrieveXPathQueryAggregate(c, "count(" + xp + ")"); }
}
