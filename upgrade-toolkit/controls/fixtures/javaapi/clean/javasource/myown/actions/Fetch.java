package myown.actions;

import com.mendix.core.Core;
import com.mendix.m2ee.api.IMxRuntimeResponse;
import com.mendix.systemwideinterfaces.core.IMendixObject;
import com.mendix.webui.CustomJavaAction;
import java.util.List;

public class Fetch extends CustomJavaAction<java.lang.Boolean>
{
	public Fetch(com.mendix.systemwideinterfaces.core.IContext context) { super(context); }

	@java.lang.Override
	public java.lang.Boolean executeAction() throws Exception
	{
		// BEGIN USER CODE
		List<IMendixObject> items = Core.createXPathQuery("//MyOwn.Item").execute(getContext());
		return Core.getMetaObject(items.get(0).getType()).isSubClassOf("System.User") && Core.getRuntimeVersion() != null;
		// END USER CODE
	}
}
