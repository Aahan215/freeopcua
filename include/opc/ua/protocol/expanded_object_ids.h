/// @author Olivier Roulet-Dubonnet 2013
/// @brief Well known attributes identifiers.
/// @license GNU LGPL
///
/// Distributed under the GNU LGPL License
/// (See accompanying file LICENSE or copy at
/// http://www.gnu.org/licenses/lgpl.html)
///

#ifndef __OPC_UA_EXPANDED_OBJECTS_IDS
#define __OPC_UA_EXPANDED_OBJECTS_IDS

#include <stdint.h>

namespace OpcUa
{
  enum class ExpandedObjectID : uint32_t
  {
    Null           = 0,
    ObjectAttribute = 354,
    VariableAttribute = 357,
    MethodAttribute = 360,
    ObjectTypeAttribute = 363,
    VariableTypeAttribute = 366 ,
    ReferenceTypeAttribute = 369,
    DataTypeAttribute = 372,
    ViewAttribute = 375,
 
    DataChangeNotification = 811,
    EventNotificationList = 812,
    StatusChangeNotification = 813,

    DataChangeFilter = 724,
    EventFilter = 727,
    AggregateFilter = 730

  };
}

#endif // __OPC_UA_BINARY_IDENTIFIERS
