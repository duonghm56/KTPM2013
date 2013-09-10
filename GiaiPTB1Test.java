import junit.framework.TestCase;


public class GiaiPTB1Test extends TestCase {
		
	public void test_giai_1_1_am1() throws Exception{
		assertEquals((double)-1, GiaiPTB1.giai(1,1));		
		
	}
	
	public void test_giai_10_am90_9() throws Exception{
		assertEquals((double)9, GiaiPTB1.giai(10,-90));
	}
	
	public void test_giai_0_0_VSN(){
		try {
			GiaiPTB1.giai(0, 0);
		} catch (Exception e) {
			assertEquals(e.getMessage(), "VSN");
		}
	}
	
	public void test_giai_0_10_VN(){
		try {
			GiaiPTB1.giai(0, 10);
		} catch (Exception e) {
			assertEquals(e.getMessage(), "VN");
		}
	}
}  
